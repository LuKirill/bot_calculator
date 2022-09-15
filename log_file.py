from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from datetime import datetime

async def log(update: Update, context: ContextTypes.DEFAULT_TYPE):
    with open('log_file.csv', "a", encoding="utf-8") as file:
        file.write(f'{update.effective_user.first_name}, {update.effective_user.id}, {update.message.text}, /'
                   f'{datetime.now().strftime("%d/%m/%y %H:%M")}\n')