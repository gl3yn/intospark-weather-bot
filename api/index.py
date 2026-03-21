import os
import telebot
from flask import Flask, request

TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot(TOKEN, threaded=False) if TOKEN else None
app = Flask(__name__)

# --- ВОТ ЭТОГО БЛОКА НЕ ХВАТАЛО ---
@bot.message_handler(commands=['start'])
def start_command(message):
    markup = telebot.types.InlineKeyboardMarkup()
    # Ссылка на твой дизайн (главная страница Vercel)
    my_app_url = "https://intospark-weather-bot.vercel.app" 
    
    btn = telebot.types.InlineKeyboardButton(
        text="Открыть Weather Pro ☁️", 
        web_app=telebot.types.WebAppInfo(url=my_app_url)
    )
    markup.add(btn)
    
    bot.reply_to(message, f"Привет, {message.from_user.first_name}! ✨\nНажми на кнопку ниже, чтобы запустить приложение.", reply_markup=markup)
# ---------------------------------

@app.route('/api', methods=['POST'])
def webhook():
    if bot and request.headers.get('content-type') == 'application/json':
        json_string = request.get_data().decode('utf-8')
        update = telebot.types.Update.de_json(json_string)
        bot.process_new_updates([update])
        return ''
    return 'OK', 200
