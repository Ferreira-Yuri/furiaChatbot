from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from dotenv import load_dotenv
import os
from comandos.start import start_comando
from comandos.noticias import noticias_comando
from comandos.clips import  clips_comando
from comandos.proximosJogos import proximosJogos_comando
from comandos.ultimosJogos import ultimosJogos_comando
from comandos.torcida import torcida_comando

# Resgata as variávies do ambiente 
load_dotenv() 
token = os.getenv("token_key")

# Inicializa o bot
app = ApplicationBuilder().token(token).build()

# Comandos do bot
app.add_handler(CommandHandler("start", start_comando))
app.add_handler(CommandHandler("noticias", noticias_comando))
app.add_handler(CommandHandler("clips", clips_comando))
app.add_handler(CommandHandler("proximosjogos", proximosJogos_comando))
app.add_handler(CommandHandler("ultimosjogos", ultimosJogos_comando))
app.add_handler(CommandHandler("torcida", torcida_comando))

print("Bot funcionando...")
app.run_polling()