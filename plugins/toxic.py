import requests
from pyrogram import filters
from pyrogram.types import Message
from ChampuMusic import app

# HuggingFace API setup
API_URL = "https://api-inference.huggingface.co/models/unitary/toxic-bert"
HEADERS = {
    "Authorization": "Bearer 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"
}

# Toxicity detection function
def is_offensive(text: str) -> bool:
    try:
        response = requests.post(API_URL, headers=HEADERS, json={"inputs": text})
        if response.status_code == 200:
            result = response.json()
            for label in result[0]:
                if label["label"] == "toxic" and label["score"] > 0.6:
                    return True
    except Exception as e:
        print(f"Toxicity check failed: {e}")
    return False

# Pyrogram handler
@app.on_message(filters.text & filters.group, group=9)
async def detect_and_delete_toxic(_, message: Message):
    if is_offensive(message.text):
        try:
            await message.delete()
            await message.reply_text(
                f"⚠️ <b>{message.from_user.mention}</b>, don’t use bad words.\n"
                "Admins may be forced to take action on repeated abuse",
                quote=True
            )
        except Exception as e:
            print(f"Failed to delete message or reply: {e}")
