import discord
import random
import aiohttp
import requests
from discord.ext import commands

##BOT_TOKEN = REDACTED FOR SECURITY REASONS AND TO PREVENT MALICIOUS USAGE
CHANNEL_ID = 1187467355585003543
LOG_CHANNEL_ID = 1187510842204368997

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

badwords = ["keys?", "raciallyoffensivewordhere"]

####    EVENTS    ####
@bot.event
async def on_ready():
    print("Booted Successfully")
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"Logged in as {bot.user.name} ({bot.user.id}) \n:wave: Hi, my name is leo and I am a bot.")
    await channel.send("Type !help for available commands")
    #await channel.send("!명령어") this commanad line will be activiated later when I decide to play with foreign languages

@bot.event
async def on_member_join(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"Everyone welcome {ctx.mention} to the Server!")
    await ctx.send(f"Hi, {ctx.mention}, Welcome to the Server!\nPlease type !help for available commands.")

@bot.event
async def on_member_remove(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    await channel.send(f"Farewell {ctx.mention}! It was nice knowing you.")

@bot.event
async def on_message(message):
    for i in badwords:
        if i in message.content:
            await message.delete()
            await message.channel.send(f"Filtered Profanity from {message.author.mention}")
            bot.dispatch('profanity', message, i)
            return
        await bot.process_commands(message)

@bot.event
async def on_profanity(message, word):
    channel = bot.get_channel(LOG_CHANNEL_ID)
    embed = discord.Embed(title = "Profanity Logged", description=f"{message.author.mention} just said ||{word}||", color=discord.Color.blurple())
    await channel.send(embed=embed)


####    COMMANDS    ####

@bot.command()
async def hello(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    await ctx.send("Hi.")

@bot.command()
async def longerphial(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    await ctx.send("2 Rousing frost \n1 Rousing Air \n10 Writhebark, Bubble Poppy, Saxifrage \n74 Hochenblume \n15 Draconic bottles ")
    await ctx.send("1. Learn Alchemy\n2. Make Refreshing Healing Potion twice(2) [7]\n3. Learn Mana potion from the Alchemist\n4. Make mana potion once(1) [10]\n5. Learn everything from the Alchemist\n6. Do three(3) Reclaim concoctions from the potions you just made [13]\n7. Make ten(10) Omnium Draconis [23]\n8. Do each of potion and phial experiments[25]\n9. Goto Ruby life pools and talk to Vialtry on top\n10. Spend your points.")

@bot.command()
async def add(ctx, x, y):
    channel = bot.get_channel(CHANNEL_ID)
    result = int(x) + int(y)
    await ctx.send(f"{x} + {y} = {result}")

@bot.command()
async def subtract(ctx, x, y):
    channel = bot.get_channel(CHANNEL_ID)
    result = int(x) - int(y)
    await ctx.send(f"{x} - {y} = {result}")

@bot.command()
async def multiply(ctx, x, y):
    channel = bot.get_channel(CHANNEL_ID)
    result = int(x) * int(y)
    await ctx.send(f"{x} * {y} = {result}")

@bot.command()
async def divide(ctx, x, y):
    channel = bot.get_channel(CHANNEL_ID)
    result = int(x) / int(y)
    await ctx.send(f"{x} / {y} = {result}")

@bot.command(aliases=['8ball', "test"])
async def _8ball(ctx, *, question):
    channel = bot.get_channel(CHANNEL_ID)
    responses = ["It is certain.",
                 "It is decidedly so.",
                 "Without a doubt.",
                 "Yes definitely.",
                 "As I see it, yes.",
                 "Ask again later.",
                 "Better not tell you now.",
                 "Cannot predict now.",
                 "Concentrate and ask again.",
                 "Don't count on it.",
                 "My reply is no.",
                 "My sources say no",
                 "Outlook not so good",
                 "Very doubtful."]
    
    await ctx.send(f"Question: {question}\nMy Response: {random.choice(responses)}")

@bot.command(aliases=["dog"])
async def random_dog(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    dog_api_url = 'https://dog.ceo/api/breeds/image/random'

    response = requests.get(dog_api_url)

    if response.status_code == 200:
        data = response.json()

        dog_picture_url = data['message']

        await ctx.send(f"I love doggos: {dog_picture_url}")
    else:
        await ctx.send("Failed to fetch data. Try again later")

@bot.command(aliases=["cat"])
async def random_cat(ctx):
    channel = bot.get_channel(CHANNEL_ID)
    cat_api_url = 'https://api.thecatapi.com/v1/images/0XYvRd7oD'

    response = requests.get(cat_api_url)

    if response.status_code == 200:
        data = response.json()
        cat_picture_url = data['url']
        await ctx.send(f"Cats are so cool: {cat_picture_url}")
    else:
        await ctx.send("Failed to fetch data. Try again later")


bot.run(BOT_TOKEN)
