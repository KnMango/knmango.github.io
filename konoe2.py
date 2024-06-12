import discord
from discord.ext import commands
import yt_dlp as youtube_dl
import asyncio
from collections import deque

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='~', intents=intents)

# 유튜브 다운로드 설정
ytdl_format_options = {
    'format': 'bestaudio/best',
    'outtmpl': '%(extractor)s-%(id)s-%(title)s.%(ext)s',
    'restrictfilenames': True,
    'noplaylist': False,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0'
}

ffmpeg_options = {
    'options': '-vn -loglevel debug',
    'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)


class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = data
        self.title = data.get('title')
        self.url = data.get('url')

    @classmethod
    async def from_url(cls, url, *, loop=None, stream=False):
        loop = loop or asyncio.get_event_loop()
        try:
            data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=not stream))
        except Exception as e:
            print(f'Error downloading video: {e}')
            return None

        if 'entries' in data:
            data = data['entries']

        return data


# 큐 관리 클래스
class MusicQueue:
    def __init__(self):
        self.queue = deque()

    def add(self, item):
        self.queue.append(item)

    def get_next(self):
        if self.queue:
            return self.queue.popleft()
        return None

    def clear(self):
        self.queue.clear()


music_queue = MusicQueue()


# 채널 이름이 "super"인지 확인하는 체크 함수
def is_in_super_channel():
    def predicate(ctx):
        return ctx.channel.name == '리듬봇-링크용'

    return commands.check(predicate)


@bot.event
async def on_ready():
    print(f'Login session checked ({bot.user})(ID: {bot.user.id})')
    print('------')


@bot.command(name='join', help='음성 채널에 접속')
@is_in_super_channel()
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send(f"{ctx.message.author.name}님, 먼저 음성 채널에 접속하십시오.")
        return
    else:
        channel = ctx.message.author.voice.channel

    await channel.connect()


@bot.command(name='play', help='링크 재생[playlist url 지원 가능]')
@is_in_super_channel()
async def play(ctx, url):
    if not ctx.voice_client:
        await ctx.send("재생 전 원하는 음성 채널에서 ~join 명령어를 사용해 주세요.")
        return

    async with ctx.typing():
        data = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
        if not data:
            await ctx.send("bad request(client.voice.play).")
            return

        if isinstance(data, list):
            for entry in data:
                source = YTDLSource(discord.FFmpegPCMAudio(entry['url'], **ffmpeg_options), data=entry)
                music_queue.add(source)
            await ctx.send(f"대기열 등록 완료: {len(data)} item(s).")
        else:
            source = YTDLSource(discord.FFmpegPCMAudio(data['url'], **ffmpeg_options), data=data)
            music_queue.add(source)
            await ctx.send(f'Now playing: {source.title}')

        if not ctx.voice_client.is_playing():
            play_next(ctx)


def play_next(ctx):
    next_track = music_queue.get_next()
    if next_track:
        ctx.voice_client.play(next_track, after=lambda e: play_next(ctx) if not e else print(f'playback err: {e}'))

@bot.command(name='next', help='큐에 새로운 트랙을 추가합니다')
@is_in_super_channel()
async def next(ctx, url):
    async with ctx.typing():
        data = await YTDLSource.from_url(url, loop=bot.loop, stream=True)
        if not data:
            await ctx.send("bad request(client.queue.add)")
            return

        if isinstance(data, list):
            for entry in reversed(data):
                source = YTDLSource(discord.FFmpegPCMAudio(entry['url'], **ffmpeg_options), data=entry)
                music_queue.add_next(source)
            await ctx.send(f"재생목록에서 {len(data)}개의 트랙을 큐의 다음에 추가했습니다.")
        else:
            source = YTDLSource(discord.FFmpegPCMAudio(data['url'], **ffmpeg_options), data=data)
            music_queue.add_next(source)
            await ctx.send(f'Next in queue: {source.title}')


@bot.command(name='queue', help='Queue 목록 출력')
@is_in_super_channel()
async def queue(ctx):
    if music_queue.queue:
        queue_list = [track.title for track in music_queue.queue]
        await ctx.send(f'Queue:\n' + '\n'.join(queue_list))
    else:
        await ctx.send('Empty queue.')


@bot.command(name='leave', help='음성 채널을 떠남')
@is_in_super_channel()
async def leave(ctx):
    if ctx.voice_client:
        music_queue.clear()
        await ctx.voice_client.disconnect()
    else:
        await ctx.send("bad request(client.disconnect).")


@bot.command(name='pause', help='재생 일시정지')
@is_in_super_channel()
async def pause(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.pause()
        await ctx.send('더 월드!!!!!')
    else:
        await ctx.send("bad request(client.pause).")


@bot.command(name='resume', help='playback 재개')
@is_in_super_channel()
async def resume(ctx):
    if ctx.voice_client and ctx.voice_client.is_paused():
        ctx.voice_client.resume()
        await ctx.send('시간은 다시 움직인다.')
    else:
        await ctx.send("bad request(client.resume).")


@bot.command(name='stop', help='재생 중단')
@is_in_super_channel()
async def stop(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        music_queue.clear()
        await ctx.send('재생을 중단합니다.')
    else:
        await ctx.send("bad request(client.stop).")


bot.run('   ')
