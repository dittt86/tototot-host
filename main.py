import discord
from discord.ext import commands
import os

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="~", intents=intents)

@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} sudah online dan siap digunakan!")

@bot.command()
async def halobot(ctx):
    await ctx.send("Halo! Saya bot Totot di sini 🤖")

@bot.command()
async def join(ctx):
    if ctx.author.voice is None:
        await ctx.send("❌ Kamu tidak sedang berada di voice channel mana pun.")
        return

    channel = ctx.author.voice.channel
    if ctx.voice_client is not None:
        await ctx.voice_client.move_to(channel)
    else:
        await channel.connect()

    await ctx.send(f"✅ Saya sudah bergabung ke voice channel **{channel}** 🎧")

@bot.command()
async def leave(ctx):
    if ctx.voice_client is None:
        await ctx.send("❌ Saya tidak sedang berada di voice channel.")
        return

    await ctx.voice_client.disconnect()
    await ctx.send("👋 Saya sudah keluar dari voice channel.")

TOKEN = os.getenv("TOKEN")
if not TOKEN:
    print("⚠️ TOKEN tidak ditemukan! Pastikan kamu sudah menambahkannya di Environment Variables hosting.")
else:
    bot.run(TOKEN)
