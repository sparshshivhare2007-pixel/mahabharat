from telegram import Update
from telegram.ext import ContextTypes

from database.users import get_user

async def profile(update:Update,context:ContextTypes.DEFAULT_TYPE):

    user = await get_user(update.effective_user.id)

    text = f"""
⚔ ᴡᴀʀʀɪᴏʀ ᴘʀᴏꜰɪʟᴇ

नाम: {user["name"]}
लेवल: {user["level"]}
XP: {user["xp"]}
धर्म: {user["dharma"]}
सुवर्ण: {user["balance"]}
"""

    await update.message.reply_text(text)
