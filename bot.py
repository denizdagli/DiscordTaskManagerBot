import discord
import os
from discord.ext import commands
from dotenv import load_dotenv
from commands import handle_add_task, handle_delete_task, handle_show_tasks, handle_complete_task

load_dotenv()

token = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Bot {bot.user} olarak giriş yaptı!")
    await bot.change_presence(activity=discord.Game(name="!add, !delete, !show, !complete"))


@bot.command()
async def add(ctx, *args):
    response = handle_add_task(args)
    await ctx.send(response)

@bot.command()
async def delete(ctx, *args):
    response = handle_delete_task(args)
    await ctx.send(response)

@bot.command()
async def show(ctx):
    response = handle_show_tasks()
    await ctx.send(response)

@bot.command()
async def complete(ctx, *args):
    response = handle_complete_task(args)
    await ctx.send(response)

bot.run(token)
