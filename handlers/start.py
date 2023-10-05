from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.inline_keyboard_button import InlineKeyboardButton as IButton
from aiogram.types.inline_keyboard_markup import InlineKeyboardMarkup
from text1 import START_TEXT
from text2 import BUTTON_TEXT
from db import queries

start_router = Router()

@start_router.message(Command("start"))
async def hello(message: types.Message):
    kb = InlineKeyboardMarkup(
        inline_keyboard=[
            [
                IButton(text="подписаться", callback_data="Sub"),
               IButton(text="Контакты", callback_data="contacts"),
               IButton(text="О нас", callback_data="about"),
               IButton(text="Наш сайт", url="https://google.com"),
            ],
       ]
    )
    await message.answer(START_TEXT, reply_markup=kb)

@start_router.callback_query(F.data == "about")
async def about(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer(BUTTON_TEXT)


@start_router.callback_query(F.data == "contacts")
async def about(callback: types.CallbackQuery):
    await callback.answer()

    await callback.message.answer("911")

@start_router.callback_query(F.data == "Sub" )
async def sub(callback: types.CallbackQuery):
    queries.subscrebu(callback.from_user.id)
