#!/usr/bin/env python
import discord, random

TOKEN = 'NTgzOTYxODQxOTYxNjY0NTI1.XPD_aA._KuB-yKCp-ELfYhmhxFyWFxOQ6U'

client = discord.Client()

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if "?" in message.content:
        msg = '{0.author.mention}, '.format(message)
        lines = []
        with open("answers.db", "r+") as f:
            for l in f:
                lines.append(l)
        msg += random.choice(lines)
        print(msg)
        await message.channel.send(msg)
    if message.content.startswith("!хз "):
        with open("answers.db", "a+") as f:
            f.write("\n"+message.content[4:])
        await message.channel.send("Мой интелект расширился благодаря тебе {0.author.mention}, ".format(message))
    if message.content == "!хз":
        msg = ""
        with open("answers.db", "r+") as f:
            for l in f:
                msg += l
        await message.channel.send("Вот список моих ответов:\n"+msg)
                

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

client.run(TOKEN)
