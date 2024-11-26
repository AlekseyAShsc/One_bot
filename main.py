import logging
from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from settings import TOKEN

logging.basicConfig(
    filename="bot.log",
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text=f"Я bot. Здравствуйте {update.message.from_user.first_name}. Поговорите со смной, я знаю Ваш ID = {update.message.from_user.id}.")
    button_list = [
        InlineKeyboardButton("Новое напоминание", callback_data="New"),
        InlineKeyboardButton("Просмотреть готовые", callback_data="Hot"),
        InlineKeyboardButton("Посмотреть архив", callback_data="Old")
    ]
    # сборка клавиатуры из кнопок `InlineKeyboardButton`
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=2))
    # отправка клавиатуры в чат для ВЕРСИИ 20.x
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Меню из двух столбцов", reply_markup=reply_markup)
    #print("Вызывн метод Start")
    #print(update.message.from_user.id)
    #update.message.reply_text("Здравствуй пользователь ...")

#async def Keybord_one(update: Update, context: ContextTypes.DEFAULT_TYPE):
#    text_message = update.message.text.upper()
#    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_message)


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text_message = update.message.text.upper()
    await context.bot.send_message(chat_id=update.effective_chat.id, text=text_message)

async def new(update: Update, context: ContextTypes.DEFAULT_TYPE):
    #text_message = update.message.text.upper()
    print("Я тут")
    await context.bot.send_message(chat_id=update.effective_chat.id, text="text_message_New")

def build_menu(buttons, n_cols,
               header_buttons=None,
               footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, [header_buttons])
    if footer_buttons:
        menu.append([footer_buttons])
    return menu






def main():
    application = ApplicationBuilder().token(TOKEN).build()
    start_handler = CommandHandler('start', start)
    echo_new = MessageHandler(filters.TEXT & ~(filters.COMMAND | filters.Regex("^New$")), new)
    echo_handler = MessageHandler(filters.TEXT & (~filters.COMMAND), echo)
    application.add_handler(start_handler)
    application.add_handler(echo_handler)
    application.add_handler(echo_new)
    logging.info("Бот стартовал.")
    application.run_polling()    

if __name__ == '__main__':
    main()