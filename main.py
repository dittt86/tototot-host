import discord
from discord.ext import commands

# Ganti dengan token kamu
TOKEN = "MTQyNDI1NjUwMjM5NDI1NzQ2MA.Gqd-3z.mBj1-NrkywON7YGaMzCt3_wxZtGk1p4qfYcQTA"

intents = discord.Intents.default()
intents.message_content = True
intents.voice_states = True

bot = commands.Bot(command_prefix="~", intents=intents, description="Totot Bot")

@bot.event
async def on_ready():
    print(f"Bot Totot sudah online sebagai {bot.user}!")

@bot.command()
async def halobot(ctx):
    await ctx.send("Halo! Saya bot Totot di sini 🤖")

@bot.command()
async def join(ctx):
    if ctx.author.voice:
        channel = ctx.author.voice.channel
        await channel.connect()
        await ctx.send(f"Saya sudah bergabung di voice channel: {channel.name}")
    else:
        await ctx.send("Kamu harus berada di voice channel dulu untuk memanggil saya!")

@bot.command()
async def leave(ctx):
    if ctx.voice_client:
        await ctx.voice_client.disconnect()
        await ctx.send("Saya sudah keluar dari voice channel.")
    else:
        await ctx.send("Saya tidak sedang berada di voice channel mana pun.")

# Template commands
for i in range(1, 11):
    async def template_command(ctx, i=i):
        await ctx.send(f"Maaf command ~template{i} belum diatur, hubungi Administrator/Admin untuk mengubah command ini.")
    bot.command(name=f"template{i}")(template_command)

bot.run(TOKEN)
