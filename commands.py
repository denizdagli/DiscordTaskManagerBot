import discord
from discord.ext import commands


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.command()
async def add_task(ctx, description: str):
    await ctx.send(f'Adding task: {description}')
    

@bot.command()
async def delete_task(ctx, task_id: int):
    await ctx.send(f'Removing task: {task_id}')

@bot.command()
async def show_tasks(ctx):
    await ctx.send('Listing tasks')

@bot.command()
async def complate_task(ctx, task_id: int):
    await ctx.send(f'coplated task: {task_id}')

