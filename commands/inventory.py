from telegram import Update
from telegram.ext import ContextTypes

from database.inventory import get_inventory

async def inventory(update:Update,context:ContextTypes.DEFAULT_TYPE):

    inv = await get_inventory(update.effective_user.id)

    if not inv:
        await update.message.reply_text("inventory खाली है")
        return

    items = "\n".join(inv["items"])

    await update.message.reply_text(
f"🎒 inventory\n\n{items}"
)
