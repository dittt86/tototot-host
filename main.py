import os
import discord
from discord.ext import commands

import discord.opus
try:
    discord.opus.load_opus('libopus.so.0')
    print("✅ Opus library berhasil dimuat")
except Exception as e:
    print("❌ Gagal memuat Opus:", e)

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True
intents.guilds = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"🤖 Bot aktif sebagai {bot.user}")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        try:
            await channel.connect()
            await ctx.send(f"🎧 Bergabung ke voice channel: **{channel}**")
        except Exception as e:
            await ctx.send("❌ Gagal bergabung ke voice channel.")
            print("Error join:", e)
    else:
        await ctx.send("🚫 Kamu harus berada di voice channel dulu!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Keluar dari voice channel.")
    else:
        await ctx.send("⚠️ Bot tidak sedang berada di voice channel.")

@bot.command()
async def hello(ctx):
    await ctx.send("Halo! Bot berjalan lancar 👋")

TOKEN = os.getenv("DISCORD_TOKEN")
if not TOKEN:
    print("❌ Token Discord tidak ditemukan! Pastikan environment variable DISCORD_TOKEN sudah diatur.")
else:
    bot.run(TOKEN)
