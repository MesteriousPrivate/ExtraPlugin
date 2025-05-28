import google.generativeai as genai
from pyrogram import filters
from pyrogram.types import Message
from ChampuMusic import app

# Gemini API config
genai.configure(api_key="AIzaSyA_a_X6a8vTKjiISMtLDkJ-azfjZg9pIqg")

# Working model (as of now)
model = genai.GenerativeModel("gemini-1.5-flash")

async def is_toxic(text: str) -> bool:
    prompt = (
        f"Kya ye message offensive ya gali type hai? (Hindi/English mix bhi ho sakta hai):\n\n"
        f"\"{text}\"\n\n"
        "Sirf 'yes' ya 'no' mein jawab do."
    )
    try:
        response = await model.generate_content_async(prompt)
        return "yes" in response.text.strip().lower()
    except Exception as e:
        print(f"[Gemini Error] {e}")
        return False

@app.on_message(filters.text & filters.group, group=9)
async def moderation(_, message: Message):
    if message.from_user and not message.from_user.is_bot:
        if await is_toxic(message.text):
            try:
                await message.delete()
                await message.reply_text(
                    f"🚫 <b>{message.from_user.mention}</b>, abusive message delete kiya gaya hai.\n\n"
                    "⚠️ Gali ya disrespect allowed nahi.\n<i>~ ShrutiBots</i>"
                )
            except Exception as e:
                print(f"❌ Error: {e}")
