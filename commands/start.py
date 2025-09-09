import sys

from utils.whitelist import whitelist_only
sys.path.append("../RoomBookingBot")

import text
from telegram import Update
from telegram.ext import ContextTypes

@whitelist_only
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    print(update.message.chat.id)
    await update.message.reply_text(text.START_MSG)
