import os
import telebot
from flask import Flask, request

TOKEN = os.environ.get('BOT_TOKEN')

bot = telebot.TeleBot(TOKEN, threaded=False)
app = Flask(__name__)

@bot.message_handler(commands=['start'])
def start(message):

    domain = request.host_url.replace('http://', 'https://')
    
    markup = telebot.types.InlineKeyboardMarkup()
    web_app = telebot.types.WebAppInfo(url=domain)
    btn = telebot.types.InlineKeyboardButton("Открыть Weather Pro ☁️", web_app=web_app)
    markup.add(btn)
    
    bot.reply_to(message, f"Привет, {message.from_user.first_name}! ✨\nНажми на кнопку, чтобы посмотреть погоду:", reply_markup=markup)

@app.route('/api', methods=['POST']) 
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
    return "Bot is running! Set your webhook to /api"
