import config
from telegram.ext import ApplicationBuilder, CommandHandler
from commands.start import start

if __name__ == '__main__':
            
    app = ApplicationBuilder().token(config.TOKEN).build()
    app.add_handler(CommandHandler("Start", start))

    app.run_polling()
    
