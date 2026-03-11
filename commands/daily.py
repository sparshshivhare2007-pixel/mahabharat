from telegram import Update
from telegram.ext import ContextTypes

from database.mongo import users

async def daily(update:Update,context:ContextTypes.DEFAULT_TYPE):

    user_id = update.effective_user.id

    reward = 100

    await users.update_one(
        {"user_id":user_id},
        {"$inc":{"balance":reward}}
    )

    await update.message.reply_text(
        f"🎁 daily reward\n\n+{reward} सुवर्ण"
    )
