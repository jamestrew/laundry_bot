import discord
from discord.ext import commands
import os
import get_weather
import random
import asyncio

client = commands.Bot(command_prefix='!')  # sets command prefix


@client.event
async def on_ready():
    print("Bot is ready.")


@client.event
async def send_alert():
    while True:
        await client.wait_until_ready()
        channel = discord.utils.get(client.guilds[0].channels, name="general")
        msg = get_weather.main(alert=True)
        if msg is not None:
            await channel.send(msg)
        await asyncio.sleep(3600)


@client.command()
async def weather(ctx):
    await ctx.send(get_weather.main())


@client.command(aliases=['8ball'])
async def _8ball(ctx):
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes - definitely.",
                 "You may rely on it.",
                 "As I see it, yes.",
                 "Most likely.",
                 "Outlook good.",
                 "Yes.",
                 "Signs point to yes.",
                 "Reply hazy, try again.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no.",
                 "Outlook not so good.",
                 "Very doubtful."
                 ]
    await ctx.send(random.choice(responses))


client.loop.create_task(send_alert())

token = os.environ.get('DISC_BOT_TOKEN')
client.run(token)
