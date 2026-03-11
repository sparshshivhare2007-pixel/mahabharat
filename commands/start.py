from telegram import Update
from telegram.ext import ContextTypes

from database.users import get_user, create_user

async def start(update:Update,context:ContextTypes.DEFAULT_TYPE):

    user = update.effective_user

    data = await get_user(user.id)

    if not data:
        await create_user(user)

    text = """
⚔ ᴍᴀʜᴀʙʜᴀʀᴀᴛ ʙᴏᴛ

कुरुक्षेत्र का युद्ध प्रारम्भ होने वाला है।

/profile
/balance
/daily
"""

    await update.message.reply_text(text)
