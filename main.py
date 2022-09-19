from bot_command import *

app = ApplicationBuilder().token("5331802360:AAH6HH63e2VAfQc71npj7PU-YU0PwPN3FbE").build()
print("server start")
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("s", start_command))

app.run_polling()
