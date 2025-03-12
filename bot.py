from aiogram import Bot, Dispatcher, types,F
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.filters import CommandStart
import asyncio

TOKEN = "6229528554:AAGUHlo0X1ffv0EzvWtwt-HzdzDlCcgyWf4"
CHANNELS = ["@kinobeks", "@prokinoes"]  # Majburiy obuna kanallari
ADMINS = [2106641907]
bot = Bot(token=TOKEN)
dp = Dispatcher()

async def check_subs(user_id: int) -> bool:
    for channel in CHANNELS:
        chat_member = await bot.get_chat_member(chat_id=channel, user_id=user_id)
        if chat_member.status in ["left", "kicked"]:
            return False
    return True

@dp.message(CommandStart())
async def start_handler(message: types.Message):
    user_id = message.from_user.id
    if not await check_subs(user_id):
        markup = InlineKeyboardMarkup(
            inline_keyboard=[
                [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
            ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        )
        await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
    else:
        await message.answer("Xush kelibsiz! Botdan foydalanishingiz mumkin.")

@dp.callback_query(lambda call: call.data == "check_subs")
async def check_subs_callback(call: types.CallbackQuery):
    user_id = call.from_user.id
    if await check_subs(user_id):
        await call.message.edit_text("Rahmat! Siz barcha kanallarga obuna bo‘lgansiz. Botdan foydalanishingiz mumkin.")
    else:
        await call.answer("Siz hali ham barcha kanallarga obuna bo‘lmagansiz!", show_alert=True)




# @dp.message(F.video | F.photo | F.document | F.audio | F.voice)
# async def get_file_id(message: types.Message):
    
#     user_id = message.from_user.id
#     if await check_subs(user_id):
#         if message.video:
#             await message.answer(f"📹 Video File ID: `{message.video.file_id}`")
#     else:
#         await message.answer('telegram kanalga obuna boling')



@dp.message(F.video | F.photo | F.document | F.audio | F.voice)
async def get_file_id(message: types.Message):
    user_id = message.from_user.id

    # Faqat adminlarga ruxsat beramiz
    if user_id in ADMINS:
        if message.video:
            await message.answer(f"📹 Video File ID: `{message.video.file_id}`")
        elif message.photo:
            await message.answer(f"🖼 Photo File ID: `{message.photo[-1].file_id}`")
        elif message.document:
            await message.answer(f"📄 Document File ID: `{message.document.file_id}`")
        elif message.audio:
            await message.answer(f"🎵 Audio File ID: `{message.audio.file_id}`")
        elif message.voice:
            await message.answer(f"🎙 Voice File ID: `{message.voice.file_id}`")
    else:
        await message.answer("🚫 Ushbu buyruq faqat adminlar uchun mavjud!")



# 📌 2️⃣ Xabar "1" bo‘lsa, oldindan olingan `file_id` dagi videoni yuborish
@dp.message(F.text == "1")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIG1WfQTZd1DdDO2STXNunJd8NTX9iSAAIbBQACB3z8USSDzPPKBDT9NgQ"
        await message.answer_video(file_id, caption="📹 Mana sizning videongiz!")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "2")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = ""
        await message.answer_video(file_id, caption="📹 Mana sizning videongiz!")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


@dp.message(F.text == "3")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = ""
        await message.answer_video(file_id, caption="📹 Mana sizning videongiz!")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)


async def main():
    print('bot ishladi....')
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())









 