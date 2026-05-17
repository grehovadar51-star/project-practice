"""
Telegram-бот — демонстрация АИС для транспортной компании
Заказчик: ООО «ЖелДорЭкспедиция»
Библиотека: pyTelegramBotAPI (telebot)
"""

import telebot
from telebot import types

TOKEN = "8708553740:AAEwiat-qhjSYlwXvYR0uFqYIMug8FIGInU"

bot = telebot.TeleBot(TOKEN)


# ==================== Главное меню ====================

@bot.message_handler(commands=['start'])
def send_welcome(message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.row("ℹ️ О проекте", "📸 Пример работы")
    keyboard.row("⭐ Преимущества", "📊 Калькулятор ROI")
    keyboard.row("🔗 Ссылки")

    text = (
        "🚛 *Добро пожаловать!*\n\n"
        "Мы — команда студентов Московского Политеха.\n"
        "Разработали АИС для автоматического определения объёма груза по фото.\n\n"
        "⚡ Возможности системы:\n"
        "• Точность детекции: 95%\n"
        "• Скорость обработки: 10 секунд\n"
        "• Готовый Docker-образ\n\n"
        "Заказчик: ООО «ЖелДорЭкспедиция»\n\n"
        "Выберите раздел:"
    )
    bot.send_message(message.chat.id, text, reply_markup=keyboard, parse_mode="Markdown")


# ==================== О проекте (с Inline-кнопками) ====================

@bot.message_handler(func=lambda msg: msg.text == "ℹ️ О проекте")
def about_project(message):
    text = (
        "ℹ️ *О проекте*\n\n"
        "АИС для транспортной компании\n\n"
        "*Заказчик:* ООО «ЖелДорЭкспедиция»\n"
        "Крупнейший транспортный оператор сборных грузов в России.\n\n"
        "*Проблема:*\n"
        "Ручные замеры ~3 минуты, ошибки 10–20%, недозагрузка до 15%.\n\n"
        "*Решение:* YOLOv8 анализирует фото за 10 сек с точностью >95%.\n\n"
        "*Технологии:* PyTorch · YOLOv8 · FastAPI · Docker · OpenCV"
    )
    
    # Inline-кнопки под сообщением
    inline = types.InlineKeyboardMarkup()
    inline.add(types.InlineKeyboardButton("🔬 Подробнее о технологиях", callback_data="tech"))
    inline.add(types.InlineKeyboardButton("📊 Экономика проекта", callback_data="econ"))
    inline.add(types.InlineKeyboardButton("🌐 Сайт проекта", url="https://grehovadar51-star.github.io/project-practice"))
    
    bot.send_message(message.chat.id, text, reply_markup=inline, parse_mode="Markdown")


# ==================== Inline-кнопки: Технологии ====================

@bot.callback_query_handler(func=lambda call: call.data == "tech")
def callback_tech(call):
    text = (
        "🔬 *Стек технологий*\n\n"
        "• Python — основной язык\n"
        "• YOLOv8 — детекция объектов\n"
        "• FastAPI — REST API\n"
        "• OpenCV — обработка изображений\n"
        "• Docker — контейнеризация\n"
        "• HTML + CSS — веб-интерфейс и сайт"
    )
    
    inline = types.InlineKeyboardMarkup()
    inline.add(types.InlineKeyboardButton("📊 Экономика проекта", callback_data="econ"))
    inline.add(types.InlineKeyboardButton("◀ Назад", callback_data="about_back"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.message_id, reply_markup=inline, parse_mode="Markdown")


# ==================== Inline-кнопки: Экономика ====================

@bot.callback_query_handler(func=lambda call: call.data == "econ")
def callback_econ(call):
    text = (
        "📊 *Экономическая эффективность*\n\n"
        "• Чистый эффект: 21 ₽/груз\n"
        "• Маржинальность: 80,8%\n"
        "• Окупаемость: < 3 месяцев\n"
        "• Годовая прибыль: > 3,8 млн ₽\n"
        "• Внедрение: 2–4 недели\n\n"
        "*Сравнение с лазерными сканерами:*\n"
        "Дешевле в 3–5 раз, быстрее в 6–12 раз."
    )
    
    inline = types.InlineKeyboardMarkup()
    inline.add(types.InlineKeyboardButton("🔬 Технологии", callback_data="tech"))
    inline.add(types.InlineKeyboardButton("◀ Назад", callback_data="about_back"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.id, reply_markup=inline, parse_mode="Markdown")


# ==================== Inline-кнопки: Назад ====================

@bot.callback_query_handler(func=lambda call: call.data == "about_back")
def callback_about_back(call):
    text = (
        "ℹ️ *О проекте*\n\n"
        "АИС для транспортной компании\n\n"
        "*Заказчик:* ООО «ЖелДорЭкспедиция»\n"
        "Крупнейший транспортный оператор сборных грузов в России.\n\n"
        "*Проблема:*\n"
        "Ручные замеры ~3 минуты, ошибки 10–20%, недозагрузка до 15%.\n\n"
        "*Решение:* YOLOv8 анализирует фото за 10 сек с точностью >95%.\n\n"
        "*Технологии:* PyTorch · YOLOv8 · FastAPI · Docker · OpenCV"
    )
    
    inline = types.InlineKeyboardMarkup()
    inline.add(types.InlineKeyboardButton("🔬 Подробнее о технологиях", callback_data="tech"))
    inline.add(types.InlineKeyboardButton("📊 Экономика проекта", callback_data="econ"))
    inline.add(types.InlineKeyboardButton("🌐 Сайт проекта", url="https://grehovadar51-star.github.io/project-practice"))
    
    bot.edit_message_text(text, call.message.chat.id, call.message.id, reply_markup=inline, parse_mode="Markdown")


# ==================== Калькулятор ROI ====================

@bot.message_handler(func=lambda msg: msg.text == "📊 Калькулятор ROI")
def calculator_start(message):
    bot.send_message(
        message.chat.id,
        "📊 *Калькулятор окупаемости*\n\n"
        "Введите количество грузов, обрабатываемых вашей компанией в месяц:\n"
        "_(например: 5000)_",
        parse_mode="Markdown"
    )
    bot.register_next_step_handler(message, calculator_result)


def calculator_result(message):
    try:
        cargo_count = int(message.text.replace(" ", "").replace(",", "."))
        if cargo_count <= 0:
            raise ValueError
        
        # Расчёты
        savings_per_cargo = 21  # руб/груз
        monthly_savings = cargo_count * savings_per_cargo
        yearly_savings = monthly_savings * 12
        roi_months = 3  # месяца
        
        text = (
            "📊 *Результат расчёта*\n\n"
            f"• Грузов в месяц: {cargo_count:,}\n"
            f"• Экономия на 1 груз: {savings_per_cargo} ₽\n"
            f"• Экономия в месяц: *{monthly_savings:,} ₽*\n"
            f"• Экономия в год: *{yearly_savings:,} ₽*\n"
            f"• Окупаемость: < {roi_months} месяцев\n\n"
            "_Расчёт основан на данных пилотного проекта.\n"
            "Для точной оценки свяжитесь с нами._"
        )
        
        inline = types.InlineKeyboardMarkup()
        inline.add(types.InlineKeyboardButton("🔄 Пересчитать", callback_data="recalc"))
        inline.add(types.InlineKeyboardButton("🌐 Сайт проекта", url="https://grehovadar51-star.github.io/project-practice"))
        
        bot.send_message(message.chat.id, text, reply_markup=inline, parse_mode="Markdown")
    
    except ValueError:
        bot.send_message(message.chat.id, "❌ Введите целое число, например: 5000")
        bot.register_next_step_handler(message, calculator_result)


@bot.callback_query_handler(func=lambda call: call.data == "recalc")
def callback_recalc(call):
    bot.send_message(call.message.chat.id, "Введите новое количество грузов в месяц:")
    bot.register_next_step_handler(call.message, calculator_result)


# ==================== Пример работы ====================

@bot.message_handler(func=lambda msg: msg.text == "📸 Пример работы")
def example_work(message):
    caption = (
        "📸 *Пример работы системы*\n\n"
        "Оператор загружает фото зоны погрузки через веб-интерфейс.\n\n"
        "Что видит система:\n"
        "• Паллета: обнаружена\n"
        "• Груз: 3 коробки\n"
        "• Объём: 1.44 м³\n"
        "Обработка заняла 10 секунд.\n\n"
    )
    
    with open("interface.png", "rb") as photo:
        bot.send_photo(message.chat.id, photo, caption=caption, parse_mode="Markdown")


# ==================== Преимущества ====================

@bot.message_handler(func=lambda msg: msg.text == "⭐ Преимущества")
def advantages(message):
    text = (
        "⭐ *Почему выбирают нашу систему*\n\n"
        "*1. Точность >95%*\n"
        "YOLOv8 обучена на реальных складских данных.\n\n"
        "*2. Скорость — 10 секунд*\n"
        "Вместо 3 минут ручного замера.\n\n"
        "*3. Простота внедрения*\n"
        "Docker-образ запускается одной командой.\n\n"
        "*4. Экономия — 21 ₽/груз*\n"
        "Окупаемость < 3 месяцев. Маржа 80,8%.\n\n"
        "*5. Объективный контроль*\n"
        "Данные сохраняются, возможен аудит.\n\n"
        "*6. Сравнение с лазерными сканерами*\n"
        "Дешевле в 3–5 раз, внедрение 2–4 недели вместо 3–6 месяцев."
    )
    
    inline = types.InlineKeyboardMarkup()
    inline.add(types.InlineKeyboardButton("📊 Калькулятор ROI", callback_data="recalc"))
    
    bot.send_message(message.chat.id, text, reply_markup=inline, parse_mode="Markdown")


# ==================== Ссылки ====================

@bot.message_handler(func=lambda msg: msg.text == "🔗 Ссылки")
def links(message):
    inline = types.InlineKeyboardMarkup()
    inline.add(types.InlineKeyboardButton("🌐 Сайт проекта", url="https://grehovadar51-star.github.io/project-practice"))
    inline.add(types.InlineKeyboardButton("🏢 ЖелДорЭкспедиция", url="https://www.jde.ru"))
    
    bot.send_message(message.chat.id, "🔗 *Полезные ссылки*", reply_markup=inline, parse_mode="Markdown")


# ==================== Обработка текста ====================

@bot.message_handler(func=lambda msg: True)
def handle_text(message):
    bot.send_message(message.chat.id, "Используйте кнопки меню или команду /start.")


# ==================== Запуск ====================

if __name__ == "__main__":
    print("Бот запущен!")
    print("Перейдите в Telegram: https://t.me/transport_ais_bot")
    bot.infinity_polling()