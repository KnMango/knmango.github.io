# 봇을 구동하기 위한 파일 임포팅
import asyncio
import discord

app = discord.Client()

# 봇 구동시 최초 실행 코드
@app.event
async def on_ready():
    game = discord.Game("마약")
    print('마약조아')
    print('Logged in') # 화면에 봇의 이름, 아이디 출력
    print('discord.Client().user.name = ', app.user.name)
    print('discord.Client().user.id = ', app.user.id)
    print('Game in Status = ', game)
    await app.change_presence(status=discord.Status.online, activity=game)
# 봇의 플레이 중인 프로그램 표시 세팅

    # await app.change_presence(game=discord.Game(name="D.Va견", type=1))

# 봇의 메시지 수신 시 코드
@app.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == "마약": # 해당 메시지 수신 시
        await message.channel.send("마약조아") # 해당 채널에 메시지 송신
        
app.run('')
