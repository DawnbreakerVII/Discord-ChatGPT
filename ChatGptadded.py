#Firstly pip install openai
'''
def chat_with_gpt(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )
    return response['choices'][0]['message']["content"]

@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return

    if message.content.startswith('!chat'):
        user_message = message.content[6:].strip()
        gpt_response = chat_with_gpt(user_message)
        await message.channel.send(f'ChatGPT: {gpt_response}')

    await Bot.process_commands(message)
'''
#In code     
from Api import *

@Bot.event
async def on_ready():
    print("Ready")

@Bot.event   
async def on_member_join(member):
    wchannel = Bot.get_channel(Channel)
    await wchannel.send(f"{member.mention} Hg")
    
@Bot.event  
async def on_member_remove(member):
    bchannel = Bot.get_channel(Channel2)
    await bchannel.send(f"{member.mention} Sg")

@Bot.command()
async def Who(ctx):
    await ctx.send("I'am Bot")
    
def chat_with_gpt(user_message):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": user_message},
        ],
    )
    return response['choices'][0]['message']["content"]

@Bot.event
async def on_message(message):
    if message.author == Bot.user:
        return

    if message.content.startswith('!chat'):
        user_message = message.content[6:].strip()
        gpt_response = chat_with_gpt(user_message)
        await message.channel.send(f'ChatGPT: {gpt_response}')

    await Bot.process_commands(message)

Bot.run(BotToken)
