from telegram.ext import Updater, CommandHandler

def greet_user(update, context):
    print("Вызывн метод Start")
    print(update)
    update.message.reply_text("Здравствуй пользователь ...")

def main():
    mybot = Updater('6896403247:AAGays5uWHp7YXbt8IyomdqinxyfCAxUCFY')

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))

    mybot.start_polling()
    mybot.idle()

main()