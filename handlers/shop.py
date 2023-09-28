import db.queries
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from db.queries import get_product


shop_router = Router()


@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Манга"),
            KeyboardButton(text="Манхва"),
            KeyboardButton(text="Манихуа"),
        ]]

    )
    await message.answer("Выберите категорию: ",
                         reply_markup=kb)

@shop_router.message(F.text == "Манга")
async def show_list(message: types.Message):
    await message.answer(get_product()[0][1])


@shop_router.message(F.text == "Манхва")
async def show_kist(message: types.Message):
    await message.answer(get_product()[1][1])


@shop_router.message(F.text == "Манихува")
async def show_kartina(message: types.Message):
    await message.answer(get_product()[2][1])