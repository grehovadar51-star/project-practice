"""
Telegram-бот проекта АИС для транспортной компании
Библиотека: pyTelegramBotAPI (telebot)
"""

import telebot
import random

TOKEN = "8708553740:AAEwiat-qhjSYlwXvYR0uFqYIMug8FIGInU"

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    """Приветствие с клавиатурой"""
    keyboard = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("/help", "/about")
    keyboard.row("/echo", "/joke")
    keyboard.row("/weather", "/survey")
    bot.reply_to(message, "👋 Привет! Я бот проекта АИС для транспортной компании.", reply_markup=keyboard)


@bot.message_handler(commands=['help'])
def send_help(message):
    """Справка по командам"""
    text = (
        "📋 *Доступные команды:*\n"
        "/start — перезапуск\n"
        "/help — справка\n"
        "/about — о проекте\n"
        "/echo \\<текст\\> — повтор текста\n"
        "/joke — случайная шутка\n"
        "/weather — погода (демо)\n"
        "/survey — опрос"
    )
    bot.reply_to(message, text, parse_mode="Markdown")


@bot.message_handler(commands=['about'])
def send_about(message):
    """Информация о проекте"""
    text = (
        "🤖 *О проекте*\n\n"
        "АИС для транспортной компании.\n"
        "Автоматизация определения объёма груза в зоне склада с помощью YOLOv8."
    )
    bot.reply_to(message, text, parse_mode="Markdown")


@bot.message_handler(commands=['echo'])
def send_echo(message):
    """Повтор текста пользователя"""
    text = message.text.replace("/echo", "").strip()
    if text:
        bot.reply_to(message, f"🔊 {text}")
    else:
        bot.reply_to(message, "ℹ️ Использование: /echo ваш текст")


@bot.message_handler(commands=['joke'])
def send_joke(message):
    """Случайная шутка"""
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? 31 OCT = 25 DEC!",
        "Багов не существует — есть недокументированные фичи.",
        "Чтобы понять рекурсию, нужно сначала понять рекурсию.",
        "Программист ставит на тумбочку два стакана: с водой и пустой.",
    ]
    bot.reply_to(message, f"😄 {random.choice(jokes)}")


@bot.message_handler(commands=['weather'])
def send_weather(message):
    """Демо-прогноз погоды"""
    text = (
        "🌤 *Прогноз погоды (демо)*\n\n"
        "📍 Москва\n"
        "🌡 +18°C\n"
        "💨 Ветер: 3 м/с\n"
        "☁️ Облачно с прояснениями"
    )
    bot.reply_to(message, text, parse_mode="Markdown")


@bot.message_handler(commands=['survey'])
def send_survey(message):
    """Демо-опрос"""
    bot.reply_to(message, "📝 *Опрос* (демо-режим)\nКак вас зовут? Напишите в ответ.", parse_mode="Markdown")


@bot.message_handler(func=lambda msg: True)
def echo_all(message):
    """Обработка всех текстовых сообщений"""
    bot.reply_to(message, f"Вы написали: {message.text}\nИспользуйте /help для списка команд.")


if __name__ == "__main__":
    print("Бот запущен!")
    print("Перейдите в Telegram: https://t.me/transport_ais_bot")
    bot.infinity_polling()