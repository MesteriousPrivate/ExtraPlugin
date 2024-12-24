import asyncio

from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

import config
from ChampuMusic import app
from ChampuMusic.utils.database import add_served_chat, get_assistant


start_txt = """**
✪ 𝐖𝐄𝐋𝐂𝐎𝐌𝐄 𝐓𝐎 𝐍𝐘 𝐂𝐑𝐄𝐀𝐓𝐈𝐎𝐍'𝐒 𝐙𝐎𝐍𝐄 ✪

➲ ᴇᴀsʏ ʜᴇʀᴏᴋᴜ ᴅᴇᴘʟᴏʏᴍᴇɴᴛ ✰  
➲ ɴᴏ ʙᴀɴ ɪssᴜᴇs ✰  
➲ ᴜɴʟɪᴍɪᴛᴇᴅ ᴅʏɴᴏs ✰  
➲ 𝟸𝟺/𝟽 ʟᴀɢ-ғʀᴇᴇ ✰

► sᴇɴᴅ ᴀ sᴄʀᴇᴇɴsʜᴏᴛ ɪғ ʏᴏᴜ ғᴀᴄᴇ ᴀɴʏ ᴘʀᴏʙʟᴇᴍs!
**"""




@app.on_message(filters.command("repo"))
async def start(_, msg):
    buttons = [
        [ 
          InlineKeyboardButton("ᴀᴅᴅ ᴍᴇ", url=f"https://t.me/{app.username}?startgroup=true")
        ],
        [
          InlineKeyboardButton("𝐍𝐚𝐧𝐝 𝐘𝐚𝐝𝐮𝐰𝐚𝐧𝐬𝐡𝐢", url="https://t.me/TMZEROO"),
          InlineKeyboardButton("𝐒𝐮𝐩𝐩𝐨𝐫𝐭 𝐆𝐫𝐨𝐮𝐩", url="https://t.me/NYCreation_Chatzone"),
          ],
               [
                InlineKeyboardButton("ꜱᴇᴄᴏɴᴅ ʙᴏᴛ", url="https://t.me/Music4vcBot"),

],
[
              InlineKeyboardButton("ᴍᴜsɪᴄ", url=f"https://t.me/Music_4_Sukoon"),
              InlineKeyboardButton("ᴄʜᴀɴɴᴇʟ", url=f"https://t.me/CreativeYdv"),
              ],
              [
              InlineKeyboardButton("ᴍᴀɴᴀɢᴍᴇɴᴛ", url=f"https://t.me/v2ddos"),
InlineKeyboardButton("ʜᴇʟᴘ ʙᴏᴛ", url=f"https://t.me/NYCREATION_BOT"),
]]
    
    reply_markup = InlineKeyboardMarkup(buttons)
    
    await msg.reply_photo(
        photo=config.START_IMG_URL,
        caption=start_txt,
        reply_markup=reply_markup
    )




@app.on_message(
    filters.command(
        ["hi", "hii", "hello", "hui", "good", "gm", "ok", "bye", "welcome", "thanks"],
        prefixes=["/", "!", "%", ",", "", ".", "@", "#"],
    )
    & filters.group
)
async def bot_check(_, message):
    chat_id = message.chat.id
    await add_served_chat(chat_id)

