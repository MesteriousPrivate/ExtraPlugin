import asyncio
import datetime
import pytz  # Time zone support

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import AUTO_GCAST, LOGGER_ID
from ChampuMusic import app
from ChampuMusic.utils.database import get_served_chats

# Convert AUTO_GCAST to boolean
AUTO_GCASTS = AUTO_GCAST.strip().lower() == "on"

PHOTO_URL = "https://envs.sh/6tX.jpg"
CAPTION = "ᴛᴀᴘ ʙᴇʟᴏᴡ ʙᴜᴛᴛᴏɴs ᴛᴏ ᴄʜᴇᴄᴋ ᴏᴜʀ ᴀʟʟ ʙᴏᴛs 💜"

BUTTONS = InlineKeyboardMarkup([
    [InlineKeyboardButton("ᴍᴜsɪᴄ𝟺ᴠᴄ", url="https://t.me/Music4vcbot?start=_tgr_ImDrXR4xZGNl"),
     InlineKeyboardButton("ᴍ𝟺ᴍᴜsɪᴄ", url="https://t.me/M4_Music_BoT?start=_tgr_8NisNvtjNTQ1")],
    
    [InlineKeyboardButton("ᴀᴀᴅʜɪʀᴀ ᴍᴜsɪᴄ", url="https://t.me/TheAadhiraBot?start=_tgr_bed7dlNmNTBl"),
     InlineKeyboardButton("ᴄʜᴀᴛ ʙᴏᴛ", url="https://t.me/NYChatBot?start=_tgr_RsYGx-4xNmQ1")],

    [InlineKeyboardButton("ʜᴇʟᴘ ʙᴏᴛ", url="https://t.me/NYCREATION_BOT?start=_tgr__gObg3Y4ZmJl")]
])


async def send_message_to_chats():
    try:
        chats = await get_served_chats()
        count = 0
        for chat_info in chats:
            chat_id = chat_info.get("chat_id")
            if isinstance(chat_id, int):  # Check if chat_id is an integer
                try:
                    await app.send_photo(
                        chat_id,
                        photo=PHOTO_URL,
                        caption=CAPTION,
                        reply_markup=BUTTONS,
                    )
                    count += 1
                    await asyncio.sleep(20)  # Sleep for 20 seconds between messages
                except Exception as e:
                    await app.send_message(LOGGER_ID, f"❌ Error sending to {chat_id}: {str(e)}")
        
        # Send a summary message
        await app.send_message(LOGGER_ID, f"✅ Broadcast completed successfully in {count} chats.")
    except Exception as e:
        await app.send_message(LOGGER_ID, f"❌ Error fetching chats: {str(e)}")


async def daily_broadcast():
    while True:
        # Convert VPS time (UTC) to Indian Standard Time (IST)
        now_utc = datetime.datetime.now(pytz.utc)
        now_ist = now_utc.astimezone(pytz.timezone("Asia/Kolkata"))

        # Set target time to 3:00 PM IST
        target_time = now_ist.replace(hour=15, minute=0, second=0, microsecond=0)

        # If current time is past today's 3 PM, set target to tomorrow
        if now_ist > target_time:
            target_time += datetime.timedelta(days=1)

        sleep_time = (target_time - now_ist).total_seconds()
        await app.send_message(LOGGER_ID, f"⏳ Next broadcast scheduled at: {target_time.strftime('%Y-%m-%d %H:%M:%S')} IST")
        
        await asyncio.sleep(sleep_time)  # Wait until 3 PM IST

        if AUTO_GCASTS:
            try:
                await send_message_to_chats()
                await app.send_message(LOGGER_ID, "✅ Broadcast sent successfully at 3 PM IST.")
            except Exception as e:
                await app.send_message(LOGGER_ID, f"❌ Broadcast error: {str(e)}")


# Start the daily broadcast task
if AUTO_GCASTS:
    asyncio.create_task(daily_broadcast())
