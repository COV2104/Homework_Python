from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import datetime

async def hi_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'Hello {update.effective_user.first_name}')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'/hi\n/time\n/help\n/sum\n/days_until_NY\n')

async def time_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f'{datetime.datetime.now().time()}')

async def sum_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    msg = update.message.text
    items = msg.split(' ')
    x = int(items[1])
    y = int(items[2])
    await update.message.reply_text(f'{x} + {y} = {x+y}')      

async def daysNY_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    now = datetime.datetime.today()
    NY = datetime.datetime(2024, 1, 1)
    d = NY-now  
    mm, ss = divmod(d.seconds, 60)
    hh, mm = divmod(mm, 60)
    await update.message.reply_text(f'До нового года: {d.days} дней {hh} ч {mm} мин {ss} сек.')          