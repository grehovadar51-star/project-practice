"""
Telegram-бот проекта АИС для транспортной компании
"""

import logging
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

logging.basicConfig(format="%(asctime)s - %(levelname)s - %(message)s", level=logging.INFO)

TOKEN = "ТВОЙ_ТОКЕН"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[KeyboardButton("/help"), KeyboardButton("/about")]]
    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)
    await update.message.reply_text("👋 Привет! Я бот проекта АИС для транспортной компании.", reply_markup=reply_markup)

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("/start /help /about /echo /joke /weather /survey")

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("АИС определения объёма груза на базе YOLOv8.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if context.args:
        await update.message.reply_text(" ".join(context.args))

async def joke(update: Update, context: ContextTypes.DEFAULT_TYPE):
    import random
    jokes = [
        "Почему программисты путают Хэллоуин и Рождество? 31 OCT = 25 DEC!",
        "Багов не существует — есть недокументированные фичи.",
        "Чтобы понять рекурсию, нужно сначала понять рекурсию."
    ]
    await update.message.reply_text(random.choice(jokes))

async def weather(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🌤 Москва: +18°C, облачно (демо)")

async def survey(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("📝 Опрос: Как вас зовут? (демо-режим)")

async def handle_text(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Используйте /help для списка команд.")

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("echo", echo))
    app.add_handler(CommandHandler("joke", joke))
    app.add_handler(CommandHandler("weather", weather))
    app.add_handler(CommandHandler("survey", survey))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_text))
    print("Бот запущен!")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()