from BanAllBot import app,START_IMG,BOT_USERNAME,BOT_NAME,LOG
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup , CallbackQuery 

START_MSG="""
ᴡᴏɪ ᴋᴏɴᴛᴏʟ **{}** , ᴋᴇɴᴀʟɪɴ ɢᴜᴇ {},
ɴɪʜ ɢᴜᴇ ᴘᴜɴʏᴀ ꜰɪᴛᴜʀ ʏɢ ʙɪꜱᴀ ʙᴜᴀᴛ ʟᴏ ᴛᴇʀᴄᴇɴɢᴀɴɢ ᴋᴀʟᴏ ᴍᴀᴜ ɴʏᴏʙᴀ ᴋʟɪᴋ ᴀᴊᴀ ᴅɪ ᴛᴏᴍʙᴏʟ ʙᴀɴᴛᴜᴀɴ.
ᴍᴀꜱᴜᴋɪɴ ɢᴜᴇ ᴋᴇ ɢʀᴜʙ ʟᴀɪɴ ʙᴜᴀᴛ ɴɢᴀɴᴄᴜʀɪɴɴʏᴀ.
"""
START_BUTTONS=InlineKeyboardMarkup (
      [
      [
         InlineKeyboardButton (text="➕ ᴛᴀᴍʙᴀʜɪɴ ᴋᴇ ɢʀᴜᴘ ʟᴜ ➕",url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
      ],
      [
         InlineKeyboardButton (text="ʙᴀɴᴛᴜᴀɴ",callback_data="help_back")
      ]
      ]
)

HELP_MSG="""
**ꜱᴇᴍᴜᴀ ᴘᴇʀɪɴᴛᴀʜ ʜᴀɴʏᴀ ᴅᴀᴘᴀᴛ ᴅɪɢᴜɴᴀᴋᴀɴ ᴅᴀʟᴀᴍ ɢʀᴜʙ**

↻ /banall : ʙᴜᴀᴛ ʙᴀɴ ꜱᴇᴍᴜᴀ ᴀɴᴀᴋ ᴘᴇʟᴇʀ ᴅᴀʀɪ ɢʀᴜʙ

↻ /unbanall : ʙᴜᴀᴛ ʟᴇᴘᴀꜱ ʙᴀɴ ꜱᴇᴍᴜᴀ ᴀɴᴀᴋ ᴘᴇʟᴇʀ ᴅᴀʀɪ ɢʀᴜʙ

↻ /kickall : ʙᴜᴀᴛ ᴋɪᴄᴋ ꜱᴇᴍᴜᴀ ᴀɴᴀᴋ ᴘᴇʟᴇʀ ᴅᴀʀɪ ɢʀᴜʙ

↻ /muteall : ʙᴜᴀᴛ ʙɪꜱᴜɪɴ ꜱᴇᴍᴜᴀ ᴀɴᴀᴋ ᴘᴇʟᴇʀ ʏᴀɴɢ ʙᴇʀɪꜱɪᴋ

↻ /unmuteall : ʙᴜᴀᴛ ʙᴜᴋᴀ ᴍᴜʟᴜᴛ ꜱᴇᴍᴜᴀ ᴀɴᴀᴋ ᴘᴇʟᴇʀ

↻ /unpinall : ʙᴜᴀᴛ ᴘɪɴ ꜱᴇᴍᴜᴀ ᴘᴇꜱᴀɴ ᴅɪ ɢʀᴜʙ ᴇʟᴜ

ᴄʀᴇᴀᴛᴇᴅ ʙʏ: [ᴀɴᴀᴋ ᴀɴᴀᴋᴀɴ ʀᴇʟᴏᴀᴅ](https://t.me/Reloadyourbrain)
"""




@app.on_message(filters.command("start"))
async def start(_,msg):
    await msg.reply_photo(
     photo=START_IMG,
     caption=START_MSG.format(msg.from_user.mention,BOT_NAME),
     reply_markup=START_BUTTONS)

@app.on_callback_query(filters.regex("help_back"))
async def help_back(_,callback_query: CallbackQuery):
    query=callback_query.message
    await query.edit_caption(HELP_MSG)    



if __name__ == "__main__":
    LOG.info("started")
    app.run()
