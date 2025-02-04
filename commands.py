import discord
from discord.ext import commands
from database import add_task, delete_task, show_tasks, complete_task


intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')
    await bot.change_presence(activity=discord.Game(name='!help'))

@bot.command()
async def add_task(ctx, description: str):
    add_task(description)
    await ctx.send(f'Adding task: {description}')
    

@bot.command()
async def delete_task(ctx, task_id: int):
    delete_task(task_id)
    await ctx.send(f'Removing task: {task_id}')

@bot.command()
async def show_tasks(ctx):
    tasks = show_tasks()
    await ctx.send(f'Listing tasks:{tasks}')

@bot.command()
async def complate_task(ctx, task_id: int):
    complete_task(task_id)
    await ctx.send(f'coplated task: {task_id}')

