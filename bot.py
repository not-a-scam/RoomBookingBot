import config
from telegram.ext import ApplicationBuilder, CommandHandler
from commands import start, book

if __name__ == '__main__':
            
    app = ApplicationBuilder().token(config.TOKEN).build()
    app.add_handler(CommandHandler("Start", start.start))
    app.add_handler(book.conv_handler)

    app.run_polling()