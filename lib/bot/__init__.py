import discord
from discord.ext import commands
import os
from lib.chat import AI
from utils.logs import log_error, log_info


intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

token = os.getenv('KEY')
welcome_channel_id = os.getenv('WELCOME_CHANNEL')
bot_name = ['wisdom keeper', '小韦同学', '韦韦', '小韦','韦斯顿']

async def send_message(destination, content):
    for i in range(0, len(content), 2000):
        await destination.send(content[i:i+2000])

@bot.event
async def on_ready():
    log_info(f'Logged in as {bot.user.name}')

@bot.event
async def on_member_join(member):
    try:
        welcome_channel = bot.get_channel(int(welcome_channel_id))
        if welcome_channel:
            await welcome_channel.send(f'🎉 欢迎加入 科协代码星球！🎉\n Hi, {member.mention} \n这里是一个致力于开发、技术分享和项目合作的社区，详细的介绍请点击[这里](https://discord.com/channels/1285977527122395298/1286365029972840499/1286971803951956009)'
                                       f'欢迎你与我们一同讨论代码、项目以及课业问题。如果你是新手，不要犹豫提问；如果你是经验丰富的开发者，'
                                       f'期待你能为社区贡献你的经验和见解。\n在加入之前，请先查看本社区[规则](https://discord.com/channels/1285977527122395298/1286365262555250779/1286370244767514725)\n对我们的活动感兴趣？点击[这里](https://discord.com/channels/1285977527122395298/1286365029972840499/1286972109569916938)'
                                       f'很高兴遇见你！😘')
            log_info(f'Member {member.mention} joined {welcome_channel.name}')

        else:
            log_error('Welcome channel not found')
    except Exception as e:
        log_error(e)

@bot.command()
async def help_me(ctx, *, question):
    try:
        ai = AI()
        answer = ai.ask(question)
        print(answer)
        await ctx.send(answer)
        log_info(f'{ctx.author} asked {question} and got {answer}')
    except Exception as e:
        log_error(e)

@bot.event
async def on_message(message):
    try:
        if message.author == bot.user:
            pass
        elif any(name in message.content.lower() for name in bot_name):
            ai = AI()
            answer = ai.ask(message.content)
            await send_message(message.channel, answer)
            log_info(f'Message from {message.author}: {message.content}, response: {answer}')
        else:
            pass # to do: decide whether record all messages or not, add other triggers to invoke AI
    except Exception as e:
        log_error(e)

    await bot.process_commands(message)

bot.run(token)