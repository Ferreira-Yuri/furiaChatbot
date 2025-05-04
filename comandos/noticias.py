from telegram import Update
from telegram.ext import ContextTypes

async def noticias_comando(update:Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Últimas nóticias da FURIA: \n"
        "Twitter: https://x.com/FURIA \n"
        "Instagram: https://www.instagram.com/furiagg \n"
    )