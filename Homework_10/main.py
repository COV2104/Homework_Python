from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from bot_commands import *

app = ApplicationBuilder().token("token").build()

app.add_handler(CommandHandler("hi", hi_command))
app.add_handler(CommandHandler("time", time_command))
app.add_handler(CommandHandler("help", help_command))
app.add_handler(CommandHandler("sum", sum_command))
app.add_handler(CommandHandler("days_until_NY", daysNY_command))
app.add_handler(CommandHandler("aphorisms", aphorisms_command))
app.add_handler(CommandHandler("english_phrases", english_phrases_command))

print('server start')
app.run_polling()