from telegram import Update
from telegram.ext import ContextTypes

from database.users import get_user

async def balance(update:Update,context:ContextTypes.DEFAULT_TYPE):

    user = await get_user(update.effective_user.id)

    await update.message.reply_text(
        f"💰 तुम्हारे पास {user['balance']} सुवर्ण हैं"
    )
