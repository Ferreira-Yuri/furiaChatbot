from telegram import Update
from telegram.ext import ContextTypes

# Dados estaticos
proximos_jogos = [
    "THE MONGOLZ x FURIA"
    "📅 Sábado, 10 de maio de 2025"
]

async def proximosJogos_comando(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📢 Próximos jogos da FURIA:\n" + "\n".join(proximos_jogos), parse_mode="Markdown")
