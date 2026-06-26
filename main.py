from discord.ui import Button, Viewimport discord
from discord.ext import commands
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

    # BUhttps://cdn.discordapp.com/attachments/1518272990016700439/1519850091207196843/992C4317-FE10-45D6-8FD8-5EB37AD86DA3.png?ex=6a3fb6f3&is=6a3e6573&hm=674e8f2d7fd61042801e02a45719dc6247a030bb076a6b3bbf8659b90b0ef18f&RAYA KENDİ RESMİNİN LİNKİNİ YAPIŞTIR
    embed.set_image(url="RESİM_LİNKİ")

    button = Button(
        label="🎫 Ticket Aç",
        style=discord.ButtonStyle.green
    )

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
