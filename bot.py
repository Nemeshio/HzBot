import discord

TOKEN = 'NTgzOTYxODQxOTYxNjY0NTI1.XPD_aA._KuB-yKCp-ELfYhmhxFyWFxOQ6U'

client = discord.Client()

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    if "?" in message.content:
        msg = '{0.author.mention}, ХЗ)'.format(message)
        print(msg)
        await message.channel.send(msg)

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)