# 디스코드 API 사용을 위해 python3 -m pip install discord 사용
import asyncio
import discord

app = discord.Client()

@app.event(on_ready):
    print(app.client.name)
    print(app.client.id)
    
@app.event(on_message):
    if 
