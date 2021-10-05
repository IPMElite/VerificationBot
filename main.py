import discord
import os
import random
import asyncio
from discord.ext.commands import Bot
import keep_alive
from discord.utils import get

token = os.environ.get('token')
bot = discord.Client()

@bot.event
async def on_message(message):
  if(message.content == "!verify"):
    guild = message.guild
    embed = discord.Embed(title="Verification", description="A new channel has been created for your verification. Welcome!", color=0xFF5733)
    await message.channel.send(embed=embed)
    rand = random.randint(1000, 9999)
    global channelname
    channelname = "user-" + str(rand)
    global verify_role
    verify_role = await guild.create_role(name = channelname)
    global verified
    verified = get(guild.roles, name="Verified")
    overwrites = {
    guild.default_role: discord.PermissionOverwrite(read_messages = False),
      verified: discord.PermissionOverwrite(read_messages = False),
      verify_role: discord.PermissionOverwrite(read_messages = True)
    }
    channel = await guild.create_text_channel(channelname, overwrites=overwrites)
    global channelid
    channelid = channel.id
    embed = discord.Embed(title="Verification", description="Please enter your Minecraft username to verify yourself.", color=0xFF5733)
    await channel.send(embed=embed)
    await message.author.add_roles(verify_role)
  if message.author.id != 894761300880662528 and "user" in message.channel.name:
    guild = message.author.guild
    await message.author.add_roles(get(guild.roles, name="Verified"))
    channel = bot.get_channel(message.channel.id)
    verify_role = get(guild.roles, name=message.channel.name)
    await channel.delete()
    await verify_role.delete()
    name_role = await guild.create_role(name = message.content)
    await message.author.add_roles(name_role)

bot.run(token)
