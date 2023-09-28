import db.queries
from aiogram import types, Router, F
from aiogram.filters import Command
from aiogram.types.keyboard_button import KeyboardButton
from aiogram.types.reply_keyboard_markup import ReplyKeyboardMarkup
from aiogram.types.reply_keyboard_remove import ReplyKeyboardRemove
from db.queries import get_products
from db.queries import get_product_by_category


shop_router = Router()
@shop_router.message(Command("shop"))
async def shop(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[
            KeyboardButton(text="Манга"),
            KeyboardButton(text="Манхва"),
            KeyboardButton(text="Манихува"),
        ]]
    )
    await message.answer("Выберите категорию: ",
                         reply_markup=kb)

@shop_router.message(F.text == "Манга")
async def show_list(message: types.Message):
    manga = get_product_by_category(1)
    kb = ReplyKeyboardRemove()
    await message.answer("Список:", reply_markup=kb)
    for f in manga:
        await message.answer(f[1])


@shop_router.message(F.text == "Манхва")
async def show_kist(message: types.Message):
    manhva = get_product_by_category(2)
    kb = ReplyKeyboardRemove()
    await message.answer("Список:", reply_markup=kb)
    for y in manhva:
        await message.answer(y[1])


@shop_router.message(F.text == "Манихува")
async def show_kartina(message: types.Message):
    manihyva = get_product_by_category(3)
    kb = ReplyKeyboardRemove()
    await message.answer("Список:", reply_markup=kb)
    for o in manihyva:
        await message.answer(o[1])