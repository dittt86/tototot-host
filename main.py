import discord
from discord.ext import commands
import yt_dlp
import asyncio
import os

# Ambil token dari environment variable Railway
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="~", intents=intents, description="Totot Bot 🎵")

# ---------- EVENTS ----------
@bot.event
async def on_ready():
    print(f"✅ Bot online sebagai {bot.user}")

# ---------- BASIC COMMANDS ----------
@bot.command()
async def halobot(ctx):
    await ctx.send("Halo! Saya bot Totot di sini 🤖")

# ---------- TEMPLATE COMMANDS ----------
for i in range(1, 11):
    async def template_func(ctx, num=i):
        await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut")
    bot.command(name=f"template{i}")(template_func)

# ---------- VOICE COMMANDS ----------
@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"🎧 Bot Totot telah bergabung ke **{channel.name}**!")
    else:
        await ctx.send("⚠️ Kamu harus berada di voice channel dulu!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Bot Totot keluar dari voice channel.")
    else:
        await ctx.send("⚠️ Bot tidak sedang berada di voice channel.")

# ---------- MUSIC COMMANDS ----------
@bot.command()
async def play(ctx, url: str):
    if not ctx.voice_client:
        if ctx.author.voice:
            await ctx.author.voice.channel.connect()
        else:
            await ctx.send("⚠️ Kamu harus berada di voice channel dulu!")
            return

    vc = ctx.voice_client
    ydl_opts = {'format': 'bestaudio'}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        audio_url = info['url']

    source = await discord.FFmpegOpusAudio.from_probe(audio_url, method='fallback')
    vc.play(source)
    await ctx.send(f"🎶 Memutar: **{info['title']}**")

@bot.command()
async def stop(ctx):
    if ctx.voice_client and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
        await ctx.send("⏹️ Musik dihentikan.")
    else:
        await ctx.send("⚠️ Tidak ada musik yang sedang diputar.")

# ---------- RUN ----------
bot.run(TOKEN)
