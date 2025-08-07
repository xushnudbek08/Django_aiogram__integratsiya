from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


# Kontakt yuborish tugmasi
qantaqt = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="📱 Kantaqtingizni yuboring", request_contact=True)]
    ],
    resize_keyboard=True
)
