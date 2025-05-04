from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

async def torcida_comando(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    pergunta = ["Quem vence o proximo confronto?"]
    times = ["FURIA 🖤", "Time Adversário 🔥", "Empate 😬"]
   
    await context.bot.send_poll(
        chat_id=update.effective_chat.id,
        question=pergunta,
        options=times,
        is_anonymous=False,
        allows_multiple_answers=False
    )
