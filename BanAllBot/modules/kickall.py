from BanAllBot import app,BOT_ID
from pyrogram import filters,enums


@app.on_message(filters.command("kickall"))
async def ban_all(_,msg):
    chat_id=msg.chat.id
 #   administrators = []
    bot=await app.get_chat_member(chat_id,BOT_ID)
    bot_permission=bot.privileges.can_restrict_members==True
#    admin_permision=administrators.privileges.can_restrict_members==True
    if bot_permission:
        async for member in app.get_chat_members(chat_id):       
            try:
                    await app.ban_chat_member(chat_id, member.user.id)
                    await msg.reply_text(f"ғᴜᴄᴋɪɴɢ ᴀʟʟ ᴍᴇᴍʙᴇʀs ᴀɴᴅ ᴛʜᴇɪʀ ᴍᴏᴍs ɪɴ ᴛʜɪs ɢʀᴏᴜᴘ {member.user.mention}")
                    await app.unban_chat_member(chat_id, member.user.id)
            except Exception:
                pass
    else:
        await msg.reply_text("don't have permissions")  
                                         
     
            
