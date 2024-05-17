import discord
from discord.ext import commands
import random

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

bot.run("///")
