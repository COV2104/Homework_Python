import telebot

bot = telebot.TeleBot('5727827246:AAEfij2U3WRjLpE6_pDXMSL9AV0CTYeAyiU')

keyboard = telebot.types.InlineKeyboardMarkup()
keyboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('C', callback_data='C'),
                telebot.types.InlineKeyboardButton('<=', callback_data = '<='),
                telebot.types.InlineKeyboardButton('/', callback_data="/"))

keyboard.row(   telebot.types.InlineKeyboardButton('7', callback_data='7'),
                telebot.types.InlineKeyboardButton('8', callback_data='8'),
                telebot.types.InlineKeyboardButton('9', callback_data = '9'),
                telebot.types.InlineKeyboardButton('*', callback_data="*"))

keyboard.row(   telebot.types.InlineKeyboardButton('4', callback_data='4'),
                telebot.types.InlineKeyboardButton('5', callback_data='5'),
                telebot.types.InlineKeyboardButton('6', callback_data = '6'),
                telebot.types.InlineKeyboardButton('-', callback_data="-"))

keyboard.row(   telebot.types.InlineKeyboardButton('1', callback_data='1'),
                telebot.types.InlineKeyboardButton('2', callback_data='2'),
                telebot.types.InlineKeyboardButton('3', callback_data = '3'),
                telebot.types.InlineKeyboardButton('+', callback_data="+")) 

keyboard.row(   telebot.types.InlineKeyboardButton(' ', callback_data='no'),
                telebot.types.InlineKeyboardButton('0', callback_data='0'),
                telebot.types.InlineKeyboardButton(',', callback_data = '.'),
                telebot.types.InlineKeyboardButton('=', callback_data="="))   

@bot.message_handler(commands=['start', 'calculater'])

def get_message(messadge):
    bot.send_message(messadge.from_user.id, reply_markup=keyboard)

bot.polling()

