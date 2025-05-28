import google.generativeai as genai
from pyrogram import filters
from pyrogram.types import Message
from ChampuMusic import app

# Gemini API Key setup
genai.configure(api_key="AIzaSyA_a_X6a8vTKjiISMtLDkJ-azfjZg9pIqg")
model = genai.GenerativeModel("gemini-pro")

# Gemini-based toxicity detector
async def is_toxic_message(text: str) -> bool:
    prompt = (
        "Kya ye message offensive ya abusive language ka use karta hai? "
        "Hindi ya English galiyo ka bhi dhyan rakho. Sirf 'yes' ya 'no' mein jawab do.\n\n"
        f"Message: {text}"
    )
    try:
        response = await model.generate_content_async(prompt)
        answer = response.text.strip().lower()
        return "yes" in answer
    except Exception as e:
        print(f"[Gemini] Error: {e}")
        return False

# Pyrogram handler for group messages
@app.on_message(filters.text & filters.group, group=9)
async def gemini_moderation(_, message: Message):
    if message.from_user and not message.from_user.is_bot:
        if await is_toxic_message(message.text):
            try:
                await message.delete()
                await message.reply_text(
                    f"🚫 <b>{message.from_user.mention}</b>, aapke message mein "
                    "offensive language detect hui hai.\n\n"
                    "⚠️ <b>Gali ya bad words ka use na karein.</b>\n"
                    "Warna admins action lene par majboor ho jayenge.\n\n"
                    "<i>~ ChampuMusic Moderation System</i>",
                    quote=True
                )
            except Exception as e:
                print(f"Failed to delete toxic message: {e}")
