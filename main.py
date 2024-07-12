import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler
from settings import TOKEN

logging.basicConfig(
    filename="bot.log",
    #format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"I'm a bot, please talk to me! Здравствуйте {update.message.from_user.first_name}. Ваш ID = {update.message.from_user.id}")
    #print("Вызывн метод Start")
    #print(update.message.from_user.id)
    #update.message.reply_text("Здравствуй пользователь ...")


def main():
    application = ApplicationBuilder().token(TOKEN).build()
    
    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)
    logging.info("Бот стартовал.")
    application.run_polling()    

if __name__ == '__main__':
    main()