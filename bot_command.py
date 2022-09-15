from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from my_ui import *
from integer import *
from log_file import log


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/help\n/int - формат ввода "/int x знак y"')

async def int_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await log(update, context)
    msg1 = update.message.text
    print(msg1)
    items = msg1.split(" ")
    x = int(items[1])
    act = items[2]
    y = int(items[3])
    await update.message.reply_text (integer(x, act, y))