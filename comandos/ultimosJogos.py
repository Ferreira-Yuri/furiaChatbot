from telegram import Update
from telegram.ext import ContextTypes

# Dados estaticos
ultimos_jogos = [
    "❌ FURIA 0 x 2 THE MONGOLZ",
    "❌ FURIA 0 x 2 VIRTUS.PRO",
    "✅ FURIA 1 x 2 COMPLEXITY",
]

async def ultimosJogos_comando(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📊 Últimos jogos da FURIA:\n" + "\n".join(ultimos_jogos), parse_mode="Markdown")