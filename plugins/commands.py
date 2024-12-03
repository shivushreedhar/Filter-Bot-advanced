import os
import asyncio
from pyrogram import Client, filters, enums
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from info import ADMINS  # List of admin IDs
from utils import get_status  # Utility function for bot status

# Command: /start
@Client.on_message(filters.command("start") & filters.incoming)
async def start(client, message):
    if message.chat.type == enums.ChatType.PRIVATE:
        buttons = [[
            InlineKeyboardButton('➕ Add Me To Your Group', url=f"http://t.me/{client.me.username}?startgroup=start"),
            InlineKeyboardButton('⚙️ Features', callback_data="features")
        ]]
        reply_markup = InlineKeyboardMarkup(buttons)
        await message.reply_text(
            f"Hello {message.from_user.mention},\n\nI am alive! Use me in groups to unlock my features.",
            reply_markup=reply_markup
        )
    else:
        await message.reply_text("Hello! I'm alive and ready to help in this group.")

# Command: /donate
@Client.on_message(filters.command("donate") & filters.incoming)
async def donate(client, message):
    await message.reply_text("💖 Support the developer by donating! Contact @YourUsername for more details.")

# Command: /shortlink
@Client.on_message(filters.command("shortlink") & filters.incoming)
async def shortlink(client, message):
    await message.reply_text("Set your shortener URL here.")

# Command: /tutorial
@Client.on_message(filters.command("tutorial") & filters.incoming)
async def tutorial(client, message):
    await message.reply_text("Provide a tutorial video or link here.")

# Command: /caption
@Client.on_message(filters.command("caption") & filters.incoming)
async def caption(client, message):
    await message.reply_text("Set a custom caption for your files.")

# Command: /template
@Client.on_message(filters.command("template") & filters.incoming)
async def template(client, message):
    await message.reply_text("Set a custom IMDB template for your files.")

# Command: /fsub
@Client.on_message(filters.command("fsub") & filters.incoming)
async def fsub(client, message):
    await message.reply_text("Set your force subscribe channel here.")

# Command: /nofsub
@Client.on_message(filters.command("nofsub") & filters.incoming)
async def nofsub(client, message):
    await message.reply_text("Force subscribe requirement removed.")

# Command: /ginfo
@Client.on_message(filters.command("ginfo") & filters.incoming)
async def ginfo(client, message):
    if message.chat.type in [enums.ChatType.GROUP, enums.ChatType.SUPERGROUP]:
        await message.reply_text(f"Group Name: {message.chat.title}\nGroup ID: {message.chat.id}")
    else:
        await message.reply_text("This command is only available in groups.")

# Command: /index
@Client.on_message(filters.command("index") & filters.incoming)
async def index(client, message):
    await message.reply_text("Index files into the bot.")

# Command: /upload
@Client.on_message(filters.command("upload") & filters.incoming)
async def upload(client, message):
    await message.reply_text("Convert media into a downloadable link.")

# Command: /font
@Client.on_message(filters.command("font") & filters.incoming)
async def font(client, message):
    await message.reply_text("Change the font style.")

# Command: /shortlink2
@Client.on_message(filters.command("shortlink2") & filters.incoming)
async def shortlink2(client, message):
    await message.reply_text("Set the shortener for the 2nd verification step.")

# Command: /shortlink3
@Client.on_message(filters.command("shortlink3") & filters.incoming)
async def shortlink3(client, message):
    await message.reply_text("Set the shortener for the 3rd verification step.")

# Command: /time2
@Client.on_message(filters.command("time2") & filters.incoming)
async def time2(client, message):
    await message.reply_text("Set the verification time for the 2nd shortener.")

# Command: /time3
@Client.on_message(filters.command("time3") & filters.incoming)
async def time3(client, message):
    await message.reply_text("Set the verification time for the 3rd shortener.")

# Command: /log
@Client.on_message(filters.command("log") & filters.incoming)
async def log(client, message):
    await message.reply_text("Set the log channel for your bot.")

# Command: /tutorial2
@Client.on_message(filters.command("tutorial2") & filters.incoming)
async def tutorial2(client, message):
    await message.reply_text("Provide a second tutorial video or link.")

# Command: /tutorial3
@Client.on_message(filters.command("tutorial3") & filters.incoming)
async def tutorial3(client, message):
    await message.reply_text("Provide a third tutorial video or link.")

# Command: /addpremium
@Client.on_message(filters.command("addpremium") & filters.user(ADMINS))
async def addpremium(client, message):
    await message.reply_text("Premium user added successfully.")

# Command: /removepremium
@Client.on_message(filters.command("removepremium") & filters.user(ADMINS))
async def removepremium(client, message):
    await message.reply_text("Premium user removed successfully.")

# Command: /myplan
@Client.on_message(filters.command("myplan") & filters.incoming)
async def myplan(client, message):
    await message.reply_text("Check your current premium plan here.")

# Command: /plan
@Client.on_message(filters.command("plan") & filters.incoming)
async def plan(client, message):
    await message.reply_text("Available plans:\n1. Basic\n2. Premium\n3. VIP")

# Command: /premiumuser
@Client.on_message(filters.command("premiumuser") & filters.user(ADMINS))
async def premiumuser(client, message):
    await message.reply_text("List of premium users:")

# Command: /broadcast
@Client.on_message(filters.command("broadcast") & filters.user(ADMINS))
async def broadcast(client, message):
    await message.reply_text("Broadcast your message to all users.")

# Command: /gbroadcast
@Client.on_message(filters.command("gbroadcast") & filters.user(ADMINS))
async def gbroadcast(client, message):
    await message.reply_text("Broadcast your message to all groups.")
