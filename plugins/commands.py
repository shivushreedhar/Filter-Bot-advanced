# © CodeXBots (Rahul)
import os, requests
import logging
import random
import asyncio
import string
import pytz
from datetime import datetime
from Script import script
from pyrogram import Client, filters, enums
from pyrogram.errors import ChatAdminRequired, FloodWait
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from database.ia_filterdb import Media, get_file_details, get_bad_files, unpack_new_file_id
from database.users_chats_db import db
from info import ADMINS, THREE_VERIFY_GAP, LOG_CHANNEL, USERNAME, VERIFY_IMG, IS_VERIFY, FILE_CAPTION, AUTH_CHANNEL, SHORTENER_WEBSITE, SHORTENER_API, SHORTENER_WEBSITE2, SHORTENER_API2, SHORTENER_API3, SHORTENER_WEBSITE3, LOG_API_CHANNEL, TWO_VERIFY_GAP, TUTORIAL, TUTORIAL2, TUTORIAL3, QR_CODE, DELETE_TIME
from utils import get_settings, save_group_settings, is_subscribed, get_size, get_shortlink, is_check_admin, get_status, temp, get_readable_time
import re
import json
import base64

@Client.on_message(filters.command("start") & filters.incoming)
async def start(client: Client, message):
    m = message
    user_id = m.from_user.id

    # Handle private chats
    if message.chat.type == enums.ChatType.PRIVATE:
        if not await db.is_user_exist(user_id):
            # Add the user to the database
            await db.add_user(user_id, message.from_user.first_name)
            await client.send_message(LOG_CHANNEL, script.NEW_USER_TXT.format(message.from_user.id, message.from_user.mention))

        # Provide welcome buttons for private chat
        buttons = [[
            InlineKeyboardButton('⇆ ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ɢʀᴏᴜᴘ ⇆', url=f'http://telegram.me/{temp.U_NAME}?startgroup=start')
        ], [
            InlineKeyboardButton('⚙ ꜰᴇᴀᴛᴜʀᴇꜱ', callback_data='features'),
            InlineKeyboardButton('💸 ᴘʀᴇᴍɪᴜᴍ', callback_data='buy_premium')
        ], [
            InlineKeyboardButton('🚫 ᴇᴀʀɴ ᴍᴏɴᴇʏ ᴡɪᴛʜ ʙᴏᴛ 🚫', callback_data='earn')
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)

        await message.reply_text(
            script.START_TXT.format(message.from_user.mention, get_status(), user_id),
            reply_markup=reply_markup,
            parse_mode=enums.ParseMode.HTML
        )
        return

    # Handle group or supergroup chats
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        status = get_status()
        aks = await message.reply_text(f"<b>🔥 ʏᴇꜱ {status},\nʜᴏᴡ ᴄᴀɴ ɪ ʜᴇʟᴘ ʏᴏᴜ??</b>")
        await asyncio.sleep(600)
        await aks.delete()
        await m.delete()

        # Log new groups
        if str(message.chat.id).startswith("-100") and not await db.get_chat(message.chat.id):
            total = await client.get_chat_members_count(message.chat.id)
            group_link = await message.chat.export_invite_link()
            user = message.from_user.mention if message.from_user else "Dear"
            await client.send_message(LOG_CHANNEL, script.NEW_GROUP_TXT.format(message.chat.title, message.chat.id, message.chat.username, group_link, total, user))
            await db.add_chat(message.chat.id, message.chat.title)
        return

    # Handle other unexpected chat types
    await message.reply_text("<b>⚠️ Unsupported chat type. Please contact support for assistance.</b>")

# Additional commands can be updated similarly to allow both PM and group-specific functionalities
