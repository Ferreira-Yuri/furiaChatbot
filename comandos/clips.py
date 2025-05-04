from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def clips_comando(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text ( 
        "🎥 Veja os últimos clipes da FURIA no YouTube:\n"
        "📺 Canal Oficial: https://www.youtube.com/@FURIA"
    )
