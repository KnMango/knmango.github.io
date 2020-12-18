# 봇을 구동하기 위한 파일 임포팅
import asyncio
import discord

app = discord.Client()

# 봇 구동시 최초 실행 코드
@app.event
async def on_ready():
    game = discord.Game("Corona SDK")
    print('3 Module(s) detected.')
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

    if message.content == "!도움말" : # 해당 메시지 수신 시
        await message.channel.send("```!도움말: 도움말 표시\n!이벤트: 이벤트 메뉴\n!반응: 키워드 반응 목록```") # 해당 채널에 메시지 송신

    if message.content.startswith("C언어 Hello World"):
        await message.channel.send('```#include <stdio.h>\n\nint main (void)\n{\n   printf("hello, World!");\n   return 0;\n}```')

# Command-이벤트
    if message.content == "!이벤트" :
        await message.channel.send('```!이벤트 목록: 이벤트 목록을 표시합니다.\n!이벤트 정보 [이름]: 해당 이벤트의 세부정보를 표시합니다.```')

    if message.content.startswith("!이벤트 목록"):
        await message.channel.send('현재 등록된 이벤트가 없습니다.')
    
    if message.content.startswith("샌즈"):
        await message.channel.send('와! 샌즈!')

    if message.content.startswith("언더테일"):
        await message.channel.send('언더테일 아시는구나!')

    if message.content.startswith("유넌병신ㅇㅈ?ㅇㅇㅈㅋㅋ"):
        await message.channel.send('```와! 이스터에그를 찾으셨군요!\n유넌교 들어가쉴?```')

    if message.content.startswith("へんたい"):
        await message.channel.send('승재요?')
    
    if message.content.startswith("상준"):
        await message.channel.send('킹갓슈퍼엠퍼러얼티밋울트라파워제네럴상준님 아시는구나!')

    if message.content.startswith("댕"):
        await message.channel.send('멍')

    if message.content == "!선택 개 고양이":
        await message.channel.send('개')

    if message.content.startswith("멍"):
        await message.channel.send('댕')

    if message.content.startswith("!다운로드"):
        await message.channel.send('https://knmango.github.io/download')

    if message.content == "와 샌즈":
        await message.channel.send('.                          ⠠⠤⠶⠶⠶⠶⠶⠶⠤⠄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠠⠾⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠷⠄⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠠⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠄⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠸⠿⠛⠉⠉⠉⠻⠿⠿⠟⠉⠉⠉⠛⠿⠇⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠸⠇⠀⠀   ⠀⠸⠿⠿⠇   wah   ⠸⠇⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠻⠶⠤⠤⠠⠿⠃⠘⠿⠄⠤⠤⠶⠟⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠀⠾⠿⠙⠶⠿⠿⠤⠤⠿⠿⠶⠏⠻⠷⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠻⠶⠜⠰⠭⠩⠍⠭⠍⠭⠱⠠⠶⠟⠀⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠠⠶⠦⠈⠻⠿⠶⠭⠘⠃⠛⠃⠫⠴⠿⠟⠡⠾⠟⠂⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠊⠉⠛⠳⠦⠈⠉⠛⠛⠛⠛⠛⠛⠉⠁⠠⠿⠋⠀⠱⠄⠀⠀⠀⠀\n⠀⠀⠀⠔⠀⠀⠄⠀⠉⠳⠦⠄⠳⠶⠶⠃⠠⠤⠞⠛⠁⠠⠂⠀⠙⠄⠀⠀⠀\n⠀⠀⠎⠀⠀⠀⠇⠀⠀⠸⠀⠏⠠⠭⠍⠈⠏⠇⠀⠀⠀⠼⠀⠀⠀⠙⠆⠀⠀\n⠀⠼⠀⠀⠀⠀⠷⠔⠒⠚⠍⠣⠸⠿⠿⠸⠋⠇⠠⠴⠚⠹⠀⠀⠀⠀⠻⠀⠀\n⠀⠻⠄⠀⠀⠰⠁⠀⠀⠀⠗⠹⠸⠿⠿⠸⠉⠇⠇⠀⠀⠈⠇⠀⠀⠀⠸⠀⠀\n⠀⠀⠙⠦⠄⠸⠀⠀⠀⠀⠱⠹⠸⠿⠿⠸⠹⠜⠀⠀⠀⠀⠇⠀⠀⠴⠋⠀⠀\n⠀⠀⠀⠈⠃⠼⠶⠄⠀⠀⠸⠾⠶⠒⠒⠚⠾⠤⠤⠤⠤⠾⠃⠶⠊⠁⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀   ⠀⠀⠀⠀⠉⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠔⠀⠶⠀⠀⠀⠀⠀⠀⠀   ⠀⠸⠇⠀⠀⠣⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠀⠇⠸⠇⠀  ⠀⠀⠀⠎⠆⠀⠀⠸⠧⠀⠀ ⠸⠀⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠰⠁⠾⠁⠀⠀ ⠀⠠⠇⠱⠀⠀⠸⠿⠀⠀ ⠀⠇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠀⠸⠀⠿⠀⠀⠀  ⠀⠸ ⠀⠸⠀⠀⠀⠿⠀  ⠀⠀⠇⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀  ⠈⠉⠉⠒⠒⠒⠒⠊⠀  ⠈⠒⠒⠒⠛⠓⠊⠉⠁⠀⠀⠀⠀⠀⠀\n⠀⠀⠀⠀⠠⠶⠶⠤⠲⠶⠀⠀⠀⠀⠀⠀⠠⠷⠶⠶⠂⠤⠶⠦⠄⠀⠀⠀⠀\n⠀⠀⠀⠀⠿⠿⠿⠿⠧⠩⠄⠀⠀⠀⠀⠀⠬⠭⠭⠱⠿⠿⠿⠿⠟')

    if message.content.startswith('일해라'):
        await message.channel.send('일해라 핫산! 일어서라 핫산!')

    if message.content == "젠카이노":
        await message.channel.send('러브라이브!')

    if message.content.startswith("!반응"):
        await message.channel.send('반응 목록!\n샌즈\n댕\n멍\n언더테일\n와 샌즈\nC언어 Hello World\n... 앞으로 더 추가 예정! 리퀘스트도 받아요~')

    if message.content.startswith("야 봇"):
        await message.channel.send('ㅇ?')

    if message.content == "구름아":
        await message.channel.send('애옹?')

    if message.content.startswith("구름아 짖어"):
        await message.channel.send('고양이는 짖을 수 없다구요!')

    if message.content.startswith("구름아 야옹"):
        await message.channel.send('애옹...')

    if message.content == "황":
        await message.channel.send('색 유미')

    if message.content == "야발":
        await message.channel.send("야발쓰지마세요 코발려나!")

    if message.content == "코발":
        await message.channel.send("코발쓰지마세요 야발려나!")

    if message.content.startswith('섹스'):
        await message.channel.send('섹스는 역시 뒷치기가 갑이지!')

    if message.content == "집가고싶다":
        await message.channel.send('오늘밤은 널 집에 보내지 않을거야 ㅎ')

    if message.content.startswith("씨발"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("시발"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("그럼 좆"):
        await message.channel.send('네')

    if message.content.startswith("그럼 좃"):
        await message.channel.send('네')

    if message.content.startswith("ㅅㅂ"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("쉬불"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("시벌"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("시펄"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("쉬펄"):
        await message.channel.send('씨발쓰지마세요!')
        
    if message.content.startswith("쉬발"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("쉬벌"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("시부랄"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("씨부랄"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("씨바"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("쉬부럴"):
        await message.channel.send('씨발쓰지마세요!')

    if message.content.startswith("안녕"):
        await message.channel.send('하위~')
    
    if message.content.startswith("하위"):
        await message.channel.send('상위~')

    if message.content.startswith("상위"):
        await message.channel.send('하위~')

    if message.content.startswith("하이"):
        await message.channel.send('로우')

    if message.content.startswith("로우"):
        await message.channel.send('하이')

    if message.content == "ㅎㅇ":
        await message.channel.send('ㅎㅇㅎㅇ~')

    if message.content == "붸":
        await message.channel.send(' 에\n    엨!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')

    if message.content.startswith("집가기싫다"):
        await message.channel.send('그럼...오늘 밤은....같이 있을래..?')

    if message.content.startswith("고자"):
        await message.channel.send('내가.... 내가 고자라니!!!!! 말도 안된다고 으헣헣헣')

    if message.content.startswith("여기가 어디오"):
        await message.channel.send('Aㅏ, 병원이오. 안심하세요. 지혈제를 썼고 응급 수술을 했어요.\n피를 많이 흘려서 이거 하마터면 큰일 날 뻔했습니다.')

    if message.content.startswith("시바"):
        await message.channel.send('씨발쓰지마세요!')
        
    if message.content.startswith("아랫쪽에 감각"):
        await message.channel.send('어느정도 완쾌 된 후에 말해주려 했는데, 선생은 앞으로....\n아이를 가질 수 없습니다.')

    if message.content == "구름이":
        await message.channel.send('https://knmango.github.io/구름껄룩.jpg')

    if message.content == "고영구름":
        await message.channel.send('https://knmango.github.io/고영구름.jpg')

    if message.content == "!app ver":
        await message.channel.send('```Current Version: dev v.0.10b\nLastest Version: dev v.0.10b```')

    if message.content == "섹":
        await message.channel.send('스')

    if message.content == "!app --ck":
        await message.channel.send('체크!\n활성 모듈 수: 1\n전체 모듈 수: 4')
        
        
app.run('NjI3MDU0NTk4MjEyOTQzODgy.XY4hlg.TLa8KL1BRaI4flF5Gv1kbqbscyY')
