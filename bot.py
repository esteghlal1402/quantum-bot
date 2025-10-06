from telegram.ext import Application, CommandHandler, MessageHandler, filters
import os
import logging

logging.basicConfig(level=logging.INFO)
TOKEN = os.getenv('BOT_TOKEN')

async def start(update, context):
    user = update.message.from_user
    await update.message.reply_text(f'🚀 سلام {user.first_name}! ربات کوانتومی فعال شد!')

async def echo(update, context):
    await update.message.reply_text(f'🤖: {update.message.text}')

async def info(update, context):
    await update.message.reply_text('🔮 ربات کوانتومی - همیشه آنلاین!')

def main():
    app = Application.builder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("info", info))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("🟢 ربات کوانتومی فعال شد!")
    app.run_polling()

if __name__ == '__main__':
    main()
