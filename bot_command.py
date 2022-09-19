from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from my_ui import *
from my_de import *


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/help\n'
                                    f'Формат вычисления целых чисел x+y\n'
                                    f'Формат вычисления рациональных чисел x/y+n/m\n'
                                    f'Формат вычисления комплексных чисел (x+yi)+(n+mi)\n'
                                    f'/s - начать вычисления!')


async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg = update.message.text
    write_line(msg)
    await update.message.reply_text(in_put_int(msg))
