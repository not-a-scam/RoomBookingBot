import sys
sys.path.append("../RoomBookingBot")

import text
from telegram import Update
from telegram.ext import ContextTypes

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    print(update.message.chat.id)
    await update.message.reply_text(text.START_MSG)