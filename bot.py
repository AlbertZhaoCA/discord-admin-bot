import discord
from dotenv import load_dotenv
from discord.ext import commands
import os

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv('KEY')
welcome_channel_id = os.getenv('WELCOME_CHANNEL')

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    try:
        print(f'Member joined: {member.mention}')
        welcome_channel = bot.get_channel(int(welcome_channel_id))
        if welcome_channel:
            print('Welcome channel found')
            await welcome_channel.send(f'🎉 欢迎加入 科协代码星球！🎉\n Hi, {member.mention} \n这里是一个致力于开发、技术分享和项目合作的社区，'
                                       f'欢迎你与我们一同讨论代码、项目以及课业问题。如果你是新手，不要犹豫提问；如果你是经验丰富的开发者，'
                                       f'期待你能为社区贡献你的经验和见解。请查看本社区[规则](https://discord.com/channels/1285977527122395298/1286365262555250779/1286370244767514725)')
        else:
            print('Welcome channel not found')
    except Exception as e:
        print(f'Error: {e}')

bot.run(token)