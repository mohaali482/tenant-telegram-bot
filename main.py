import requests
from telegram import *
from telegram.ext import *
from plugins.strings import *
from plugins.settings import API





def start(update: Update, context: CallbackContext):
    update.message.reply_text(
        welcome_message.format(username = update.message.from_user.username, chat_id = update.effective_chat.id),
        parse_mode=ParseMode.HTML
    )


def main():
    updater = Updater(API)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('start', start))

    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()