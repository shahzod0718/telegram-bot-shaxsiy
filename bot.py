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
        await message.answer("Xush kelibsiz! Botdan foydalanishingiz mumkin. Kino kodini kiriting")

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
        await message.answer_video(file_id, caption="🎬 Mana sizning videongiz!")
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
        file_id = "BAACAgQAAxkBAAIHa2fRIxCRTGQY-fs75Tivfs8Wta_qAAIvEAACCmLIUZP-1XCNJPUzNgQ"
        await message.answer_video(file_id, caption="🎬 Bedlend ovchilar")
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
        file_id = "BAACAgIAAxkBAAIHbWfRI1pdE44sc-YE0RKdP0cBNq58AAL3BwACr-UwSRfiLCQQIoEpNgQ"
        await message.answer_video(file_id, caption="🎬 Gabbarning qaytishi")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "4")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHfWfRJASwDCQY7rWQrvdqyJEyxm4nAAIjUgACM10gSoLkwdLooLofNgQ"
        await message.answer_video(file_id, caption="🎬 Polaroid (Ujas kino)")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "5")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIHjGfRJDROLoPIvPwPM16xOBxRLTi6AAJsFQAC8p3oUOq2_GBhyJguNgQ"
        await message.answer_video(file_id, caption="🎬Mening Aybim")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "6")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHkmfRJH9CioCyr33hfk6ZsT-i61y_AAKJTAACM10oSjRL9jpYa7ClNgQ"
        await message.answer_video(file_id, caption="🎬 Mening buzulgan tuyim")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "7")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHlmfRJLmROHCMghnIEi0oGqnPH3DyAAK3TwAC904oSkjSAk8h59bSNgQ"
        await message.answer_video(file_id, caption="🎬 Ancharted")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "8")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHmGfRJO7pbaSAMe9ZULxlI9c8GzBqAAIWTQACyrb4SpaQEEFqm3tdNgQ"
        await message.answer_video(file_id, caption="🎬 Stuardessalar")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "9")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHmmfRJRLBlFPcfwG4b_yDbom8gZ8TAAKZAAOHuqBI8wa9Z2XGLdI2BA"
        await message.answer_video(file_id, caption="🎬 Ajoyib Poyga 2⃣")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "10")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIHnGfRJU8T0iqCiUcmfwxB04ZoUG4MAAKNFgACFCIRU7jBO4zf3meINgQ"
        await message.answer_video(file_id, caption="🎬 Raqam 810 ")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "11")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHnmfRJZnLHvfre7HelPVlCq5J5FskAAIPVAAC2zCxSRwptfsXmwL9NgQ"
        await message.answer_video(file_id, caption="🎬 X-Men 9(G'aroyib Odamlar 9)")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "12")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHoGfRJb9Z6c1PVFt6_yIHvD9xvE-jAALIIQAC9YBYSvpARF0PQx9CNgQ"
        await message.answer_video(file_id, caption="🎬 Ta'tildagi qotil")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "13")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHomfRJk7mh7qMMWqLTptJv6eMP6jvAAJeWgACnZ7BSpSTyYrXhaAUNgQ"
        await message.answer_video(file_id, caption="🎬 T 34")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "14")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHpGfRJnS5qQ4gue_b9DHhlU5s3z_5AAIwVgACTMlQSmigedCvU_iONgQ"
        await message.answer_video(file_id, caption="🎬 Jannat onalar oyog'i ostida")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "15")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHpmfRJp0mfKLLW-DMCB1oqcW4LYZuAAKzTgACzA1QSyc6Me36F5uENgQ"
        await message.answer_video(file_id, caption="🎬 Ko'rinmas Oltiovlon")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "16")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHqGfRJsPRFsECLq97WdLQfNaE8uQDAAJicAACGXNBSL0L7N2jLfpiNgQ"
        await message.answer_video(file_id, caption="🎬 Panda operatsiyasi")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "17")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHqmfRJuRxc0DTmYDMIxIUPwcbuRj7AAIoUQACwYKRSAIsDAF6YGiUNgQ"
        await message.answer_video(file_id, caption="🎬 Qurol yaroq qiroli")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "18")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHrGfRJxIu03ft2880HbRzvNiSpEZ8AAK_WgACa7RZSCVTkAVp1fCiNgQ"
        await message.answer_video(file_id, caption="🎬 Yetti opa singil")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "19")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHrmfRJzrFv-ddfVjJ85aR9G7moWh3AALIWAACk174S88wwW3sTaklNgQ"
        await message.answer_video(file_id, caption="🎬 Mikki Mous tuzog'i")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "20")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHsGfRJ12jN2b0D2uEsCc5Gx__Vt1xAAJ5WAACM5eASsi0mTY1wHEQNgQ"
        await message.answer_video(file_id, caption="🎬 Moviy qo'ng'iz")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "21")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHsmfRJ3wyi-Pufqwcwn5FqpEE9wVWAAIhWwACt_hASsh6URclaMknNgQ"
        await message.answer_video(file_id, caption="🎬 Kommando")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "22")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHtGfRJ7I1vxi7YeRBv6sLI5RdDBbUAAIlWwACt_hASrccuM_6QKuvNgQ"
        await message.answer_video(file_id, caption="🎬 Kommando 2")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "23")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHtmfRJ9hZYIYJEosY4QABr5kFn79x5wACKVsAArf4QEqWXdiCXArIrzYE"
        await message.answer_video(file_id, caption="🎬 Kommando 3")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "24")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHuGfRJ_c9ibAPLtxM-EQOOGzluvylAAK1UwAC8PwISu4BKrDuWOcSNgQ"
        await message.answer_video(file_id, caption="🎬 Yovvoyilar sayyorasi")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "25")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHumfRKAu-O2GF1D_QIcPrMIPYzP4hAAJFTAACXsTwSQYKSJc3vW5_NgQ"
        await message.answer_video(file_id, caption="🎬 Mening qizim josus 2")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)
@dp.message(F.text == "26")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgEAAxkBAAIHvGfRKDkcarTGvnyZrrx66wkrsUmFAAJKAQACiTNwRywirtrDVNImNgQ"
        await message.answer_video(file_id, caption="🎬 Kelajak Jangi / Ertangi Urush")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "27")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHvmfRKGzY7k4GYPe8gLiWBe4apFWtAAJzTwACiZyZSZs0C8ZvU_DPNgQ"
        await message.answer_video(file_id, caption="🎬 Dedpul va Rasamaxa")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "28")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIHwGfRKIm9HOR-xu6VCLhfbFgP9twvAALTFwACVTcQUTmFzrqYxg5jNgQ"
        await message.answer_video(file_id, caption="🎬 Zaxiradagi politsiyachi")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "29")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgQAAxkBAAIHwmfRKOSfJKwgPsuJWk9uLjLRUPYgAALJFwAC0EoQUVSlmmOTpqAVNgQ"
        await message.answer_video(file_id, caption="🎬 Gʻaroyib odam")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "30")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHxWfRKRDSlXyYJQfQFyrNNgABa40UegACcUwAAifh2UjYcAu_nC9YujYE"
        await message.answer_video(file_id, caption="🎬 Greyhound ")
    else:
        await message.answer('telegram kanalga obuna boling')
        # markup = InlineKeyboardMarkup(
        #     inline_keyboard=[
        #         [InlineKeyboardButton(text=f"🔗 {channel}", url=f"https://t.me/{channel[1:]}")] for channel in CHANNELS
        #     ] + [[InlineKeyboardButton(text="✅ Tekshirish", callback_data="check_subs")]]
        # )
        # await message.answer("Botdan foydalanish uchun quyidagi kanallarga obuna bo‘ling:", reply_markup=markup)

@dp.message(F.text == "31")
async def send_video(message: types.Message):
    user_id = message.from_user.id
    
    if await check_subs(user_id):  # Faqat obuna bo‘lganlarga javob qaytaradi
        file_id = "BAACAgIAAxkBAAIHx2fRKTCDyuvIluoudQ2T-ZbX0GixAAIKSgACk92xSBCUKpTxyUBSNgQ"
        await message.answer_video(file_id, caption="🎬 Isquvar 4 Megre")
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









 
