import discord
from dotenv import load_dotenv
from discord.ext import commands
import os
from ai import AI

load_dotenv()

intents = discord.Intents.default()
intents.members = True
intents.message_content = True


bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv('KEY')
welcome_channel_id = os.getenv('WELCOME_CHANNEL')
bot_name = ['wisdom keeper', '小韦同学', '韦韦同学', '韦韦', '小韦','韦斯顿']

async def send_message(destination, content):
    for i in range(0, len(content), 2000):
        await destination.send(content[i:i+2000])

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
            await welcome_channel.send(f'🎉 欢迎加入 科协代码星球！🎉\n Hi, {member.mention} \n这里是一个致力于开发、技术分享和项目合作的社区，详细的介绍请点击[这里](https://discord.com/channels/1285977527122395298/1286365029972840499/1286971803951956009)'
                                       f'欢迎你与我们一同讨论代码、项目以及课业问题。如果你是新手，不要犹豫提问；如果你是经验丰富的开发者，'
                                       f'期待你能为社区贡献你的经验和见解。\n再加入之前，请先查看本社区[规则](https://discord.com/channels/1285977527122395298/1286365262555250779/1286370244767514725)\n对我们的活动感兴趣？点击[这里](https://discord.com/channels/1285977527122395298/1286365029972840499/1286972109569916938)')
        else:
            print('Welcome channel not found')
    except Exception as e:
        print(f'Error: {e}')

@bot.command()
async def help_me(ctx, *, question):
    print(f'Question: {question}')
    ai = AI()
    answer = ai.ask(question)
    print(answer)
    await ctx.send(answer)

@bot.event
async def on_message(message):
    print(f'Message from {message.author}: {message.content}')
    if message.author == bot.user:
        print('Bot message')

    elif any(name in message.content.lower() for name in bot_name):
        print(f'Question: {message.content}')
        ai = AI()
        answer = ai.ask(message.content)
        print(answer)
        await send_message(message.channel, answer)

    await bot.process_commands(message)



bot.run(token)
