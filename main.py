# from calculator import simple_calc
from bot_command import *

app = ApplicationBuilder().token("5623249318:AAH6tPRV3gG9ZsD8QqYXxUuVBIfcvZOvk28").build()
print("server start")
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("int", int_command))

app.run_polling()