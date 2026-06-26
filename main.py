import discord
from discord.ext import commands
from discord.ui import Button, View
import os

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"{bot.user} aktif!")

@bot.command()
async def ping(ctx):
    await ctx.send("🏓 Pong!")
@bot.command()
async def panel(ctx):
    embed = discord.Embed(
        title="🌌 VOID ÇETESİ | DESTEK PANELİ",
        description="""
👋 VOID ÇETESİ destek sistemine hoş geldin.

🎫 Destek almak için aşağıdaki butona bas.
⚡ Yetkili ekip en kısa sürede seninle ilgilenecektir.
🕷️ Gereksiz ticket açmayınız.
""",
        color=0x8000ff
    )

    # R
    embed.set_image(url="RESİM_LİNKİ")

    button = Button(
        label="🎫 Ticket Aç",
        style=discord.ButtonStyle.green
    )embed.set_image(url="RESİM_LİNKİ")

    async def button_callback(interaction):
        await interaction.response.send_message(
            "🎫 Ticket sistemi henüz kurulmadı, yakında eklenecek!",
            ephemeral=True
        )

    button.callback = button_callback

    view = View()
    view.add_item(button)

    await ctx.send(embed=embed, view=view)
TOKEN = os.getenv("TOKEN")
bot.run(TOKEN)
