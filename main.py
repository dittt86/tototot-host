import discord
from discord.ext import commands
import os

# ====== KONFIGURASI DASAR BOT ======
# Token diambil dari environment variable agar aman di hosting
TOKEN = os.getenv("DISCORD_TOKEN")

# Aktifkan intents agar bot bisa membaca pesan & voice state
intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.voice_states = True

# Prefix command
bot = commands.Bot(command_prefix="~", intents=intents, description="Bot Totot by Aditya Dzaki")

# ====== EVENT SAAT BOT ONLINE ======
@bot.event
async def on_ready():
    print(f"✅ Bot {bot.user} sudah online dan siap digunakan!")


# ====== COMMAND UTAMA ======
@bot.command()
async def halobot(ctx):
    """Bot menyapa user"""
    await ctx.send("Halo! Saya bot Totot di sini 🤖")


# ====== COMMAND JOIN / LEAVE VC ======
@bot.command()
async def join(ctx):
    """Bot bergabung ke voice channel user"""
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"🎧 Bergabung ke voice channel: **{channel}**")
    else:
        await ctx.send("🚫 Kamu harus berada di voice channel terlebih dahulu agar bot bisa join!")


@bot.command()
async def leave(ctx):
    """Bot keluar dari voice channel"""
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("👋 Bot telah keluar dari voice channel.")
    else:
        await ctx.send("❌ Bot tidak sedang berada di voice channel mana pun.")


# ====== TEMPLATE COMMAND (1–10) ======
@bot.command()
async def template1(ctx):
    await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut.")

@bot.command()
async def template2(ctx):
    await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut.")

@bot.command()
async def template3(ctx):
    await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut.")

@bot.command()
async def template4(ctx):
    await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut.")

@bot.command()
async def template5(ctx):
    await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut.")

@bot.command()
async def template6(ctx):
    await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut.")

@bot.command()
async def template7(ctx):
    await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut.")

@bot.command()
async def template8(ctx):
    await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut.")

@bot.command()
async def template9(ctx):
    await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut.")

@bot.command()
async def template10(ctx):
    await ctx.send("Maaf command tersebut belum diatur, hubungi Administrator/Admin untuk mengubah command tersebut.")


# ====== JALANKAN BOT ======
if __name__ == "__main__":
    if TOKEN is None:
        print("❌ ERROR: Environment variable DISCORD_TOKEN belum diatur!")
        print("Gunakan: export DISCORD_TOKEN='token_bot_kamu' (Linux/Mac)")
        print("Atau di Windows: setx DISCORD_TOKEN \"token_bot_kamu\"")
    else:
        bot.run(TOKEN)
