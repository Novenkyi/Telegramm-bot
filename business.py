from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton,ReplyKeyboardRemove, InlineKeyboardMarkup, InlineKeyboardButton, InlineQueryResultArticle
import requests
import random
from bs4 import BeautifulSoup
from aiogram.types import ParseMode
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
import pandas as pd
import openpyxl


"""""""""""""""""""""""""""Эксель"""""""""""""""""""""""""""
excel_data_df = pd.read_excel('1.xls', sheet_name='TDSheet')
column_names = excel_data_df.columns
ekshon_kam = excel_data_df.iloc[226:230]
excel_data_df = pd.read_excel('1.xls', sheet_name='TDSheet')
first_column_name = excel_data_df.columns[0]
df = pd.DataFrame(excel_data_df)
df.to_excel('output.xlsx', index=False)
#print('--------------------------')
excel_data_df1 = pd.read_excel('output.xlsx')
first_column_name1 = excel_data_df1.columns[0]
f1 = excel_data_df1.columns[12]


keyword1 = "Беспроводная гарнитура Apple AirPods Max"
AAM = excel_data_df[excel_data_df[first_column_name].str.contains(keyword1, na=False)]
outputAAM = ""
for index, row in AAM.iterrows():
    outputAAM += f"Model: {row[first_column_name]}\n"
    outputAAM += f"Price: {row[f1]}\n"
    outputAAM += f"\n"

keyword3 = "Apple AirPods 2"
pods2 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword3, na=False)]
outputpods2 = ""
for index, row in pods2.iterrows():
    outputpods2 += f"Model: {row[first_column_name]}\n"
    outputpods2 += f"Price: {row[f1]}\n"
    outputpods2 += f"\n"

keyword4 = "Apple AirPods 3"
pods3 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword4, na=False)]
outputpods3 = ""
for index, row in pods3.iterrows():
    outputpods3 += f"Model: {row[first_column_name]}\n"
    outputpods3 += f"Price: {row[f1]}\n"
    outputpods3 += f"\n"

keyword6 = "наушник "
komplekt = excel_data_df[excel_data_df[first_column_name].str.contains(keyword6, na=False)]
outputkomplekt = ""
for index, row in komplekt.iterrows():
    outputkomplekt += f"Model: {row[first_column_name]}\n"
    outputkomplekt += f"Price: {row[f1]}\n"
    outputkomplekt += f"\n"

keyword7 = "Кейс на AirPods"
keisair = excel_data_df[excel_data_df[first_column_name].str.contains(keyword7, na=False)]
outputkeisair = ""
for index, row in keisair.iterrows():
    outputkeisair += f"Model: {row[first_column_name]}\n"
    outputkeisair += f"Price: {row[f1]}\n"
    outputkeisair += f"\n"

keyword8 = "Экшн-камера"
ekshon = excel_data_df[excel_data_df[first_column_name].str.contains(keyword8, na=False)]
outputekshon = ""
for index, row in ekshon.iterrows():
    outputekshon += f"Model: {row[first_column_name]}\n"
    outputekshon += f"Price: {row[f1]}\n"
    outputekshon += f"\n"

keyword13 = "Пылесос"
pilesos = excel_data_df[excel_data_df[first_column_name].str.contains(keyword13, na=False)]
outputpilesos = ""
for index, row in pilesos.iterrows():
    outputpilesos += f"Model: {row[first_column_name]}\n"
    outputpilesos += f"Price: {row[f1]}\n"
    outputpilesos += f"\n"


keyword14 = "Фен"
phen = excel_data_df[excel_data_df[first_column_name].str.contains(keyword14, na=False)]
outputphen = ""
for index, row in phen.iterrows():
    outputphen += f"Model: {row[first_column_name]}\n"
    outputphen += f"Price: {row[f1]}\n"
    outputphen += f"\n"

keyword15 = "Cтилус"
stilus = excel_data_df[excel_data_df[first_column_name].str.contains(keyword15, na=False)]
outputstilus = ""
for index, row in stilus.iterrows():
    outputstilus += f"Model: {row[first_column_name]}\n"
    outputstilus += f"Price: {row[f1]}\n"
    outputstilus += f"\n"

keyword16 = "клавиатура"
klava = excel_data_df[excel_data_df[first_column_name].str.contains(keyword16, na=False)]
outputklava = ""
for index, row in klava.iterrows():
    outputklava += f"Model: {row[first_column_name]}\n"
    outputklava += f"Price: {row[f1]}\n"
    outputklava += f"\n"

keyword18 = "мышь"
mouse = excel_data_df[excel_data_df[first_column_name].str.contains(keyword18, na=False)]
outputmouse = ""
for index, row in mouse.iterrows():
    outputmouse += f"Model: {row[first_column_name]}\n"
    outputmouse += f"Price: {row[f1]}\n"
    outputmouse += f"\n"

keyword17 = "Apple Magic"
AM = excel_data_df[excel_data_df[first_column_name].str.contains(keyword17, na=False)]
outputAM = ""
for index, row in AM.iterrows():
    outputAM += f"Model: {row[first_column_name]}\n"
    outputAM += f"Price: {row[f1]}\n"
    outputAM += f"\n"


keyword21 = "Apple Watch SE"
AWSE = excel_data_df[excel_data_df[first_column_name].str.contains(keyword21, na=False)]
outputAWSE = ""
for index, row in AWSE.iterrows():
    outputAWSE += f"Model: {row[first_column_name]}\n"
    outputAWSE += f"Price: {row[f1]}\n"
    outputAWSE += f"\n"

keyword = "Apple Watch Series 8"
AW8 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword, na=False)]
outputAW8 = ""
for index, row in AW8.iterrows():
    outputAW8 += f"Model: {row[first_column_name]}\n"
    outputAW8 += f"Price: {row[f1]}\n"
    outputAW8 += f"\n"

keyword22 = "Apple Watch Series 7"
AW7 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword22, na=False)]
outputAW7 = ""
for index, row in AW7.iterrows():
    outputAW7 += f"Model: {row[first_column_name]}\n"
    outputAW7 += f"Price: {row[f1]}\n"
    outputAW7 += f"\n"

keyword23 = "Apple Watch Ultra"
AWU = excel_data_df[excel_data_df[first_column_name].str.contains(keyword23, na=False)]
outputAWU = ""
for index, row in AWU.iterrows():
    outputAWU += f"Model: {row[first_column_name]}\n"
    outputAWU += f"Price: {row[f1]}\n"
    outputAWU += f"\n"

keyword31 = "iPhone 11"
iphone11 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword31, na=False)]
outputiphone11 = ""
for index, row in iphone11.iterrows():
    outputiphone11 += f"Model: {row[first_column_name]}\n"
    outputiphone11 += f"Price: {row[f1]}\n"
    outputiphone11 += f"\n"

keyword32 = "iPhone 12"
iphone12 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword32, na=False)]
outputiphone12 = ""
for index, row in iphone12.iterrows():
    outputiphone12 += f"Model: {row[first_column_name]}\n"
    outputiphone12 += f"Price: {row[f1]}\n"
    outputiphone12 += f"\n"

keyword36 = "iPhone 13"
ip13 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword36, na=False)]
outputip13 = ""
for index, row in ip13.iterrows():
    outputip13 += f"Model: {row[first_column_name]}\n"
    outputip13 += f"Price: {row[f1]}\n"
    outputip13 += f"\n"

keyword40 = "iPhone 14"
ip14 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword40, na=False)]
outputip14 = ""
for index, row in ip14.iterrows():
    outputip14 += f"Model: {row[first_column_name]}\n"
    outputip14 += f"Price: {row[f1]}\n"
    outputip14 += f"\n"

keyword44 = "iPhone SE \(2020\)"
IPSE2020 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword44, na=False)]
outputIPSE2020 = ""
for index, row in IPSE2020.iterrows():
    outputIPSE2020 += f"Model: {row[first_column_name]}\n"
    outputIPSE2020 += f"Price: {row[f1]}\n"
    outputIPSE2020 += f"\n"

keyword45 = "iPhone SE \(2022\)"
IPSE2022 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword45, na=False)]
IPSE2022 = IPSE2022.drop(
    columns=["Unnamed: 1", "Unnamed: 2", "Unnamed: 3", "Unnamed: 4", "Unnamed: 5", "Unnamed: 6", "Unnamed: 7",
                 "Unnamed: 8", "Unnamed: 9", "Unnamed: 10", "Unnamed: 11"])
outputIPSE2022 = ""
for index, row in IPSE2022.iterrows():
    outputIPSE2022 += f"Model: {row[first_column_name]}\n"
    outputIPSE2022 += f"Price: {row[f1]}\n"
    outputIPSE2022 += f"\n"

keyword25 = "iPad \(2020\)"
ipad2020 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword25, na=False)]
outputipad2020 = ""
for index, row in ipad2020.iterrows():
    outputipad2020 += f"Model: {row[first_column_name]}\n"
    outputipad2020 += f"Price: {row[f1]}\n"
    outputipad2020 += f"\n"

keyword26 = "iPad \(2021\)"
ipad2021 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword26, na=False)]
outputipad2021 = ""
for index, row in ipad2021.iterrows():
    outputipad2021 += f"Model: {row[first_column_name]}\n"
    outputipad2021 += f"Price: {row[f1]}\n"
    outputipad2021 += f"\n"

keyword27 = "iPad \(2022\)"
ipad2022 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword27, na=False)]
outputipad2022 = ""
for index, row in ipad2022.iterrows():
    outputipad2022 += f"Model: {row[first_column_name]}\n"
    outputipad2022 += f"Price: {row[f1]}\n"
    outputipad2022 += f"\n"

keyword28 = "iPad Air \(2022\)"
ipadair2022 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword28, na=False)]
outputipadair2022 = ""
for index, row in ipadair2022.iterrows():
    outputipadair2022 += f"Model: {row[first_column_name]}\n"
    outputipadair2022 += f"Price: {row[f1]}\n"
    outputipadair2022 += f"\n"

keyword29 = "iPad mini \(2021\)"
ipadmini2021 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword29, na=False)]
outputipadmini2021 = ""
for index, row in ipadmini2021.iterrows():
    outputipadmini2021 += f"Model: {row[first_column_name]}\n"
    outputipadmini2021 += f"Price: {row[f1]}\n"
    outputipadmini2021 += f"\n"

keyword30 = "iPad Pro"
ipadpro = excel_data_df[excel_data_df[first_column_name].str.contains(keyword30, na=False)]
outputipadpro = ""
for index, row in ipadpro.iterrows():
    outputipadpro += f"Model: {row[first_column_name]}\n"
    outputipadpro += f"Price: {row[f1]}\n"
    outputipadpro += f"\n"

keyword15 = "Cтилус"
stilus = excel_data_df[excel_data_df[first_column_name].str.contains(keyword15, na=False)]
outputstilus = ""
for index, row in stilus.iterrows():
    outputstilus += f"Model: {row[first_column_name]}\n"
    outputstilus += f"Price: {row[f1]}\n"
    outputstilus += f"\n"

keyword9 = "Sony "
sony = excel_data_df[excel_data_df[first_column_name].str.contains(keyword9, na=False)]
outputsony = ""
for index, row in sony.iterrows():
    outputsony += f"Model: {row[first_column_name]}\n"
    outputsony += f"Price: {row[f1]}\n"
    outputsony += f"\n"

keyword12 = "ортативная"
audio = excel_data_df[excel_data_df[first_column_name].str.contains(keyword12, na=False)]
outputaudio = ""
for index, row in audio.iterrows():
    outputaudio += f"Model: {row[first_column_name]}\n"
    outputaudio += f"Price: {row[f1]}\n"
    outputaudio += f"\n"

keyword5 = "Беспроводная Bluetooth"
bluetooth = excel_data_df[excel_data_df[first_column_name].str.contains(keyword5, na=False)]
outputbluetooth = ""
for index, row in bluetooth.iterrows():
    outputbluetooth += f"Model: {row[first_column_name]}\n"
    outputbluetooth += f"Price: {row[f1]}\n"
    outputbluetooth += f"\n"

keyword10 = "Apple TV"
atv = excel_data_df[excel_data_df[first_column_name].str.contains(keyword10, na=False)]
outputatv = ""
for index, row in atv.iterrows():
    outputatv += f"Model: {row[first_column_name]}\n"
    outputatv += f"Price: {row[f1]}\n"
    outputatv += f"\n"

keyword46 = "Mac mini"
macmini = excel_data_df[excel_data_df[first_column_name].str.contains(keyword46, na=False)]
outputmini = ""
for index, row in macmini.iterrows():
    outputmini += f"Модель: {row[first_column_name]}\n"
    outputmini += f"Цена: {row[f1]}\n"
    outputmini += f"\n"


keyword47 = "MacBook Air"
macair = excel_data_df[excel_data_df[first_column_name].str.contains(keyword47, na=False)]
outputair = ""
for index, row in macair.iterrows():
    outputair += f"Модель: {row[first_column_name]}\n"
    outputair += f"Цена: {row[f1]}\n"
    outputair += f"\n"

keyword48 = "MacBook Pro"
macpro = excel_data_df[excel_data_df[first_column_name].str.contains(keyword48, na=False)]
outputpro = ""
for index, row in macpro.iterrows():
    outputpro += f"Модель: {row[first_column_name]}\n"
    outputpro += f"Цена: {row[f1]}\n"
    outputpro += f"\n"

keyword333 = "iPhone 15"
ip15 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword333, na=False)]
outputip15 = ""
for index, row in ip15.iterrows():
    outputip15 += f"Model: {row[first_column_name]}\n"
    outputip15 += f"Price: {row[f1]}\n"
    outputip15 += f"\n"

keyword141 = "Apple Watch Series 9"
AW8 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword141, na=False)]
outputAW9 = ""
for index, row in AW8.iterrows():
    outputAW9 += f"Model: {row[first_column_name]}\n"
    outputAW9 += f"Price: {row[f1]}\n"
    outputAW9 += f"\n"

keyword143 = "Apple Watch SE Gen 2"
SEG2 = excel_data_df[excel_data_df[first_column_name].str.contains(keyword143, na=False)]
outputSEG2 = ""
for index, row in AW8.iterrows():
    outputSEG2 += f"Model: {row[first_column_name]}\n"
    outputSEG2 += f"Price: {row[f1]}\n"
    outputSEG2 += f"\n"
"""""""""""""""""""""""""""Основа"""""""""""""""""""""""""""
TOKEN = "6921576474:AAEZCpMnImbRlkDvZ4agu6GYMwclcRdtLfc"
bot = Bot(token=TOKEN)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
b131 = KeyboardButton('/назад')
b324 = KeyboardButton('/каталог')
b4 = KeyboardButton('/заказ')
b5 = KeyboardButton('/отзывы')
b6 = KeyboardButton('/проблема с товаром')
global kb_client3
kb_client3 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
kb_client3.add(b324).add(b4).add(b5).add(b6)
class OrderState(FSMContext):
    pass

# Замените 'YOUR_USER_ID' на ваш ID в Telegram
YOUR_USER_ID = 899486823


async def on_startup(_):
    print('Бот онлайн')


"""""""""""""""""""""""""""Начальное меню"""""""""""""""""""""""""""
@dp.message_handler(commands=['start', 'help'])
async def url_command(message: types.Message):
    b324 = KeyboardButton('/каталог')
    b4 = KeyboardButton('/заказ')
    b5 = KeyboardButton('/отзывы')
    b6 = KeyboardButton('/проблема с товаром')
    kb_client = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_client.add(b324).add(b4).add(b5).add(b6)
    await message.answer("Привет!👋 \n Я бот для заказа техники.🤖 \n\n Вот моё меню: \n /каталог \n /заказ \n /отзывы \n /проблема с заказом", reply_markup=kb_client )

@dp.message_handler(commands=['назад'])
async def url_command(message: types.Message):
    await message.answer("🤖 \n Вот моё меню: \n /каталог \n /заказ \n /отзывы \n /проблема с заказом", reply_markup=kb_client3)

"""""""""""""""""""""""""""Каталог"""""""""""""""""""""""""""

@dp.message_handler(commands='каталог')
async def url_command(message: types.Message):
    b1 = KeyboardButton('/ЭК')
    b2 = KeyboardButton('/ИП')
    b3 = KeyboardButton('/УК')
    b7 = KeyboardButton('/ТВ')
    b9 = KeyboardButton('/C')
    b10 = KeyboardButton('/KM')
    b11 = KeyboardButton('/AP')
    b12 = KeyboardButton('/AW')
    b13 = KeyboardButton('/D')
    b14 = KeyboardButton('/ID')
    b15 = KeyboardButton('/IP')
    b16 = KeyboardButton('/M')
    kb_client1 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_client1.row(b1,b2,b3).row(b7,b9,b10).row(b11, b12,b13).row(b16,b14,b15).add(b131)
    await message.answer("Какую технику ты хочешь заказать?")
    await message.answer('Список: \n ✅ЭК - Экшн-камеры \n ✅ИП - Игровые приставки, геймпады и комплектующие '
                         '\n ✅УК -  Умные колонки, Портативная акустика \n '
                         '✅ТВ - TV приставки, Стационарные медиаплееры '
                         '\n ✅C - Стилусы \n ✅КМ - Клавиатуры, Мыши'
                         '\n ✅АР - AirPods \n ✅AW - AppleWatch \n ✅D - Dyson \n ✅ID - IPad \n ✅IP - IPhone \n ✅M - Mac' , reply_markup=kb_client1)


"""""""""""""""""""""""""""Apple Watch"""""""""""""""""""""""""""
@dp.message_handler(commands=['AW'])
async def url_command(message: types.Message):
    b17 = KeyboardButton('/SE')
    b18 = KeyboardButton('/SEGEN2')
    b19 = KeyboardButton('/S7')
    b20 = KeyboardButton('/S8')
    b21 = KeyboardButton('/S9')
    b22 = KeyboardButton('/U')
    global kb_client2
    kb_client2 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_client2.row(b17, b18, b19).row(b20, b21, b22).add(b131)
    await message.answer("Какая модель вам нужна?", reply_markup=kb_client2)


@dp.message_handler(commands=['SE'])
async def url_command(message: types.Message):
    await message.answer(outputAWSE, reply_markup=kb_client2)

@dp.message_handler(commands=['S7'])
async def url_command(message: types.Message):
    await message.answer(outputAW7, reply_markup=kb_client2)

@dp.message_handler(commands=['S8'])
async def url_command(message: types.Message):
    await message.answer(outputAW8, reply_markup=kb_client2)

@dp.message_handler(commands=['U'])
async def url_command(message: types.Message):
    await message.answer(outputAWU, reply_markup=kb_client2)

@dp.message_handler(commands=['S9'])
async def url_command(message: types.Message):
    await message.answer(outputAW9, reply_markup=kb_client2)

@dp.message_handler(commands=['SEGEN2'])
async def url_command(message: types.Message):
    await message.answer(outputSEG2, reply_markup=kb_client2)

"""""""""""""""""""""""""""Mac"""""""""""""""""""""""""""
@dp.message_handler(commands=['M'])
async def url_command(message: types.Message):
    b50 = KeyboardButton('/mini')
    b51 = KeyboardButton('/Air')
    b52 = KeyboardButton('/Pro')
    global kb_client8
    kb_client8 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_client8.row(b50, b51, b52).add(b131)
    await message.answer("Какая модель вам нужна?", reply_markup=kb_client8)


@dp.message_handler(commands=['mini'])
async def url_command(message: types.Message):
    await message.answer(outputmini, reply_markup=kb_client8)

@dp.message_handler(commands=['Air'])
async def url_command(message: types.Message):
    await message.answer(outputair, reply_markup=kb_client8)

@dp.message_handler(commands=['Pro'])
async def url_command(message: types.Message):
    await message.answer(outputpro, reply_markup=kb_client8)

"""""""""""""""""""""""""""Ipad"""""""""""""""""""""""""""

@dp.message_handler(commands=['ID'])
async def url_command(message: types.Message):
    b40 = KeyboardButton('/iPad2020')
    b41 = KeyboardButton('/iPad2021')
    b42 = KeyboardButton('/iPad2022')
    b43 = KeyboardButton('/iPadAir2022')
    b44 = KeyboardButton('/iPadMini2021')
    b45 = KeyboardButton('/iPadPro')
    global kb_client8
    kb_client8 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_client8.row(b40, b41, b42).row(b43, b44, b45).add(b131)
    await message.answer("Какая модель тебе нужна?", reply_markup=kb_client8)



@dp.message_handler(commands=['iPad2020'])
async def url_command(message: types.Message):
    await message.answer(outputipad2020, reply_markup=kb_client8)

@dp.message_handler(commands=['iPad2021'])
async def url_command(message: types.Message):
    await message.answer(outputipad2021, reply_markup=kb_client8)

@dp.message_handler(commands=['iPad2022'])
async def url_command(message: types.Message):
    await message.answer(outputipad2022, reply_markup=kb_client8)

@dp.message_handler(commands=['iPadAir2022'])
async def url_command(message: types.Message):
    await message.answer(outputipadair2022, reply_markup=kb_client8)

@dp.message_handler(commands=['iPadMini2021'])
async def url_command(message: types.Message):
    await message.answer(outputipadmini2021, reply_markup=kb_client8)

#@dp.message_handler(commands=['iPadPro'])
#async def url_command(message: types.Message):
    #await message.answer(outputipadpro, reply_markup=kb_client8)

"""""""""""""""""""""""""""AirPods"""""""""""""""""""""""""""
@dp.message_handler(commands=['AP'])
async def url_command(message: types.Message):
    b24 = KeyboardButton('/MAX')
    b25 = KeyboardButton('/2')
    b26 = KeyboardButton('/3')
    b27 = KeyboardButton('/наушник')
    b28 = KeyboardButton('/кейс')
    global kb_client4
    kb_client4 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_client4.row(b24, b25, b26).row(b27, b28).add(b131)
    await message.answer("Какая модель тебе нужна?", reply_markup=kb_client4)

@dp.message_handler(commands=['MAX'])
async def url_command(message: types.Message):
    await message.answer(outputAAM, reply_markup=kb_client4)

@dp.message_handler(commands=['2'])
async def url_command(message: types.Message):
    await message.answer(outputpods2, reply_markup=kb_client4)

@dp.message_handler(commands=['3'])
async def url_command(message: types.Message):
    await message.answer(outputpods3, reply_markup=kb_client4)

@dp.message_handler(commands=['наушник'])
async def url_command(message: types.Message):
    await message.answer(outputkomplekt, reply_markup=kb_client4)

@dp.message_handler(commands=['кейс'])
async def url_command(message: types.Message):
    await message.answer(outputkeisair, reply_markup=kb_client4)

"""""""""""""""""""""""""""ЭкшнКамера"""""""""""""""""""""""""""

@dp.message_handler(commands=['ЭК'])
async def url_command(message: types.Message):
    await message.answer(outputekshon, reply_markup=kb_client3)

"""""""""""""""""""""""""""Cтилус"""""""""""""""""""""""""""

@dp.message_handler(commands=['C'])
async def url_command(message: types.Message):
    await message.answer(outputstilus, reply_markup=kb_client3)

"""""""""""""""""""""""""""ТВ"""""""""""""""""""""""""""

@dp.message_handler(commands=['ТВ'])
async def url_command(message: types.Message):
    await message.answer(outputatv, reply_markup=kb_client3)

"""""""""""""""""""""""""""Приставки"""""""""""""""""""""""""""

@dp.message_handler(commands=['ИП'])
async def url_command(message: types.Message):
    await message.answer(outputsony, reply_markup=kb_client3)

"""""""""""""""""""""""""""Колонки"""""""""""""""""""""""""""

@dp.message_handler(commands=['УК'])
async def url_command(message: types.Message):
    await message.answer(outputaudio, reply_markup=kb_client3)

"""""""""""""""""""""""""""Dyson"""""""""""""""""""""""""""

@dp.message_handler(commands=['D'])
async def url_command(message: types.Message):
    b29 = KeyboardButton('/пылесос')
    b30 = KeyboardButton('/фен')
    global kb_client5
    kb_client5 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_client5.row(b29, b30).add(b131)
    await message.answer("Какой продукт тебе нужен?", reply_markup=kb_client5)

@dp.message_handler(commands=['пылесос'])
async def url_command(message: types.Message):
    await message.answer(outputpilesos, reply_markup=kb_client5)

@dp.message_handler(commands=['фен'])
async def url_command(message: types.Message):
    await message.answer(outputphen, reply_markup=kb_client5)

"""""""""""""""""""""""""""Клавиатура мышь"""""""""""""""""""""""""""

@dp.message_handler(commands=['KM'])
async def url_command(message: types.Message):
    #await message.answer(outputklava)
    await message.answer(outputmouse)
    await message.answer(outputAM, reply_markup=kb_client3)

"""""""""""""""""""""""""""ipone"""""""""""""""""""""""""""

@dp.message_handler(commands=['IP'])
async def url_command(message: types.Message):
    b24 = KeyboardButton('/11')
    b25 = KeyboardButton('/12')
    b26 = KeyboardButton('/13')
    b27 = KeyboardButton('/14')
    b28 = KeyboardButton('/15')
    b30 = KeyboardButton('/SE2020')
    b31 = KeyboardButton('/SE2022')
    global kb_client6
    kb_client6 = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    kb_client6.row(b24, b25, b26,b27).row(b28, b30, b31).add(b131)
    await message.answer("Какая модель тебе нужна?", reply_markup=kb_client6)

@dp.message_handler(commands=['11'])
async def url_command(message: types.Message):
    await message.answer(outputiphone11, reply_markup=kb_client6)

@dp.message_handler(commands=['12'])
async def url_command(message: types.Message):
    await message.answer(outputiphone12, reply_markup=kb_client6)


@dp.message_handler(commands=['13'])
async def url_command(message: types.Message):
    await message.answer(outputip13, reply_markup=kb_client6)

#@dp.message_handler(commands=['14'])
#async def url_command(message: types.Message):
    #await message.answer(outputip14, reply_markup=kb_client6)

@dp.message_handler(commands=['15'])
async def url_command(message: types.Message):
    await message.answer(outputip15, reply_markup=kb_client6)

@dp.message_handler(commands=['SE2020'])
async def url_command(message: types.Message):
    await message.answer(outputIPSE2020, reply_markup=kb_client6)

@dp.message_handler(commands=['SE2022'])
async def url_command(message: types.Message):
    await message.answer(outputIPSE2022, reply_markup=kb_client6)


"""""""""""""""""""""""""""ЗАказ"""""""""""""""""""""""""""

# Создаем словарь для хранения данных пользователей
user_data = {}
@dp.message_handler(commands=['заказ'], state="*")
async def start_order(message: types.Message, state: FSMContext):
    # Устанавливаем состояние пользователя в "waiting_for_name"
    await state.set_state("waiting_for_name")
    await message.reply("Привет! Спасибо, что выбрали нас! Введите ваше имя:")
@dp.message_handler(lambda message: message.text, state="waiting_for_name")
async def get_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_data[user_id] = {"name": message.text}
    # Устанавливаем состояние пользователя в "waiting_for_tovar"
    await state.update_data(name=message.text)
    await state.set_state("waiting_for_tovar")
    await message.reply(f"Отлично, _{message.text}_! Теперь введите товар, который хотите приобрести с подробным описанием (модель, цвет, количество памяти и др.):", parse_mode=types.ParseMode.MARKDOWN)
@dp.message_handler(lambda message: message.text, state="waiting_for_tovar")
async def get_tovar(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_data[user_id]["tovar"] = message.text
    # Устанавливаем состояние пользователя в "waiting_for_address"
    await state.update_data(tovar=message.text)
    await state.set_state("waiting_for_address")
    await message.reply(f"Спасибо! Как вы хотите забрать заказ? \n _🤝Самовывоз_ - бесплатно - Метро Лианозово \nили \n🚙 _Доставка_ - 1000 рублей?", parse_mode=types.ParseMode.MARKDOWN)
@dp.message_handler(lambda message: message.text, state="waiting_for_address")
async def get_address(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_data[user_id]["address"] = message.text
    # Получаем данные пользователя из состояния
    user_info = await state.get_data()
    # Отправляем сообщение менеджеру
    formatted_message = f"Сообщение о заказе от {message.from_user.first_name} {message.from_user.last_name} (@{message.from_user.username}): \n\n Имя: {user_info['name']}\n Товар: {user_info['tovar']}\nАдрес: {message.text}"
    await bot.send_message(chat_id=YOUR_USER_ID, text=formatted_message, parse_mode=ParseMode.MARKDOWN)
    # Сбрасываем состояние пользователя
    await state.finish()
    await message.reply("Спасибо! Ваш заказ принят. В течение часа с вами свяжется наш менеджер.")
    await message.answer("🤖 \n Вот моё меню: \n /каталог \n /заказ \n /отзывы \n /проблема с заказом",reply_markup=kb_client3)

"""""""""""""""""""""""""""Проблема"""""""""""""""""""""""""""
user_data = {}
@dp.message_handler(commands=['проблема'], state="*")
async def start_order(message: types.Message, state: FSMContext):
    # Устанавливаем состояние пользователя в "waiting_for_name"
    await state.set_state("waiting_for_name1")
    await message.reply("Здравствуйте! Извините за приченённые неудобства! Введите ваше имя:")
@dp.message_handler(lambda message: message.text, state="waiting_for_name1")
async def get_name(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_data[user_id] = {"name": message.text}
    # Устанавливаем состояние пользователя в "waiting_for_tovar"
    await state.update_data(name=message.text)
    await state.set_state("waiting_for_tovar1")
    await message.reply(f"Отлично, _{message.text}_! Теперь введите товар, который вы приобретали с подробным описанием (модель, цвет, количество памяти и др.):", parse_mode=types.ParseMode.MARKDOWN)
@dp.message_handler(lambda message: message.text, state="waiting_for_tovar1")
async def get_tovar(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_data[user_id]["tovar"] = message.text
    # Устанавливаем состояние пользователя в "waiting_for_address"
    await state.update_data(tovar=message.text)
    await state.set_state("waiting_for_address1")
    await message.reply(f"Спасибо. Теперь опишите подробно проблему", parse_mode=types.ParseMode.MARKDOWN)
@dp.message_handler(lambda message: message.text, state="waiting_for_address1")
async def get_address(message: types.Message, state: FSMContext):
    user_id = message.from_user.id
    user_data[user_id]["address"] = message.text
    # Получаем данные пользователя из состояния
    user_info = await state.get_data()
    # Отправляем сообщение менеджеру
    formatted_message = f"Сообщение о проблеме с товаром от {message.from_user.first_name} {message.from_user.last_name} (@{message.from_user.username}): \n\n Имя: {user_info['name']}\n Товар: {user_info['tovar']}\nПроблема: {message.text}"
    await bot.send_message(chat_id=YOUR_USER_ID, text=formatted_message, parse_mode=ParseMode.MARKDOWN)
    # Сбрасываем состояние пользователя
    await state.finish()
    await message.reply("Спасибо! Ваше обращение принято. В течение часа с вами свяжется наш менеджер.")
    await message.answer("🤖 \n Вот моё меню: \n /каталог \n /заказ 💸 \n /отзывы \n /проблема с заказом",reply_markup=kb_client3)


executor.start_polling(dp, skip_updates=True, on_startup=on_startup)