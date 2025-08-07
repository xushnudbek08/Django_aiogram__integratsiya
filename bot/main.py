import os
import django
import asyncio

from aiogram import Bot, Dispatcher, types, F
from aiogram.enums import ParseMode
from aiogram.types import Message, ReplyKeyboardRemove
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.filters import CommandStart
from aiogram.client.default import DefaultBotProperties
from asgiref.sync import sync_to_async

# Django muhitini sozlash
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings") # Django loyihasining sozlamalar faylini ko'rsatish
django.setup()

# Django model
from main.models import TelegramUser
from bot.config import BOT_TOKEN, id # Bot tokeni va adminlar ID larini import qilish
from bot.buttons import qantaqt

# Bot va Dispatcher
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
dp = Dispatcher(storage=MemoryStorage())

# Holatlar
class RegisterState(StatesGroup):
    waiting_for_phone = State()

# /start komandasi
@dp.message(CommandStart())
async def start_handler(message: Message, state: FSMContext):
    user_exists = await sync_to_async(
        TelegramUser.objects.filter(telegram_id=message.from_user.id).exists
    )()
    if user_exists:
        await message.answer("✅ Siz allaqachon ro'yxatdan o'tgansiz.")
    else:
        await message.answer("📱 Iltimos, telefon raqamingizni yuboring:", reply_markup=qantaqt)
        await state.set_state(RegisterState.waiting_for_phone)

# Telefon raqamni qabul qilish
@dp.message(RegisterState.waiting_for_phone, F.contact)
async def get_phone(message: Message, state: FSMContext):
    contact = message.contact
    await sync_to_async(TelegramUser.objects.create)(
        telegram_id=message.from_user.id,
        full_name=message.from_user.full_name,
        username=message.from_user.username,
        phone_number=contact.phone_number
    )
    await message.answer("✅ Ro'yxatdan o'tdingiz!", reply_markup=ReplyKeyboardRemove())
    await state.clear()

# Agar contact bo'lmasa
@dp.message(RegisterState.waiting_for_phone)
async def wrong_format(message: Message):
    await message.answer("❗ Iltimos, tugma orqali telefon raqamingizni yuboring.")

# Default handler
@dp.message()
async def default_handler(message: Message):
    await message.answer("👋 Salom, bot ishga tushdi!")

# Botni ishga tushirish
async def main():
    for admin_id in id:
        try:
            await bot.send_message(admin_id, "🚀 Bot ishga tushdi")
        except Exception as e:
            print(f"Admin [{admin_id}] ga habar yuborilmadi: {e}")

    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Xatolik yuz berdi: {e}")
