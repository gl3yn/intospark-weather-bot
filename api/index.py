from flask import Flask, request
import telebot
from telebot import types

TOKEN = 'bot_token'
APP_URL = 'https://твой-проект.vercel.app' 

bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):
    markup = types.InlineKeyboardMarkup()
    web_app = types.WebAppInfo(url=APP_URL)
    btn = types.InlineKeyboardButton("Открыть погоду ☁️", web_app=web_app)
    markup.add(btn)
    
    bot.reply_to(message, f"Привет, {message.from_user.first_name}! Это Intospark Weather. Нажми кнопку ниже:", reply_markup=markup)

@app.route('/', methods=['POST'])
def webhook():
    if request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    else:
        return 'Forbidden', 403

@app.route('/')
def index():
    return "Bot is running"