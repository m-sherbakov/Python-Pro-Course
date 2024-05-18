import discord
from discord.ext import commands
import random
import matplotlib.pyplot as plt
import bot_logic
import os
import requests

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=discord.Intents.default())

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Привет! Я бот {bot.user}!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def sum(ctx, a, b):
    await ctx.send(f"Сумма = {int(a) + int(b)}")

@bot.command()
async def minus(ctx, a, b):
    await ctx.send(f"Разность = {int(a) - int(b)}")

@bot.command()
async def div(ctx, a, b):
    await ctx.send(f"Деление дало значение = {int(a) // int(b)}")

@bot.command()
async def multi(ctx, a, b):
    await ctx.send(f"Умножение равно = {int(a) * int(b)}")

@bot.command()
async def expon(ctx, a, b):
    await ctx.send(f"Получилось значение = {int(a) ** int(b)}")

@bot.command()
async def randnum(ctx, a, b):
    random_number = random.choice([int(a), int(b)])
    await ctx.send(f"Рандомное число = {random_number}")

@bot.command()
async def bitcoin(ctx):
    price_history = bot_logic.get_price_history()
    plt.plot(price_history)
    plt.savefig('bitcoin_price.png')
    await ctx.send(f"Цена bitcoin: {round(price_history[-1])}")
    await ctx.send(file=discord.File('bitcoin_price.png'))

@bot.command()
async def crypto(ctx):
    img_name = random.choice(os.listdir('images'))
    with open(f'images/{img_name}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

def get_duck_image_url():
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.command('duck')
async def duck(ctx):
    '''По команде duck вызывает функцию get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command()
async def nft(ctx):
    img_name_nft = random.choice(os.listdir('nft'))
    if img_name_nft == "lega1.png" or img_name_nft == "lega2.png":
        for i in range(5):
            await ctx.send('Legendary NFT!')
    with open(f'nft/{img_name_nft}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)


bot.run("///")
