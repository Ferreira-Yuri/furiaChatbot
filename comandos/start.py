from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def start_comando(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text (
        "🔥 Aqui você acompanha tudo sobre os jogos do nosso time do coração — "
        "notícias, clipes e interação com a torcida, tudo em um só lugar. "
        "Bora torcer juntos pela FURIA! 💛🖤"
    )
