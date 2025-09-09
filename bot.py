import config
import logging
from telegram.ext import ApplicationBuilder, CommandHandler
from commands import start, book, check, adduser, register, removeuser, setgroup

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

if __name__ == '__main__':
            
    app = ApplicationBuilder().token(config.TOKEN).build()
    app.add_handler(CommandHandler("Start", start.start))
    app.add_handler(book.conv_handler)
    app.add_handler(check.conv_handler)
    app.add_handler(CommandHandler("adduser", adduser.adduser))
    app.add_handler(CommandHandler("register", register.register))
    app.add_handler(CommandHandler("removeuser", removeuser.removeuser))
    app.add_handler(CommandHandler("setgroup", setgroup.setgroup))

    app.run_polling()
