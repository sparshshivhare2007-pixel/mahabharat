from telegram.ext import ApplicationBuilder, CommandHandler

from config import BOT_TOKEN

from commands.start import start
from commands.help import help_cmd
from commands.profile import profile
from commands.balance import balance
from commands.daily import daily
from commands.join import join
from commands.attack import attack
from commands.special import special
from commands.duel import duel
from commands.inventory import inventory
from commands.shop import shop
from commands.temple import temple
from commands.leaderboard import leaderboard


def main():

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_cmd))
    app.add_handler(CommandHandler("profile", profile))
    app.add_handler(CommandHandler("balance", balance))
    app.add_handler(CommandHandler("daily", daily))
    app.add_handler(CommandHandler("join", join))
    app.add_handler(CommandHandler("attack", attack))
    app.add_handler(CommandHandler("special", special))
    app.add_handler(CommandHandler("duel", duel))
    app.add_handler(CommandHandler("inventory", inventory))
    app.add_handler(CommandHandler("shop", shop))
    app.add_handler(CommandHandler("temple", temple))
    app.add_handler(CommandHandler("leaderboard", leaderboard))

    print("ᴍᴀʜᴀʙʜᴀʀᴀᴛ ʙᴏᴛ ɪs ʀᴜɴɴɪɴɢ")

    app.run_polling()


if __name__ == "__main__":
    main()
