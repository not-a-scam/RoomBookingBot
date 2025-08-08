import sys
sys.path.append("../RoomBookingBot")

from text import START_MESSAGE
from telegram import Update
from telegram.ext import ContextTypes

'''Start Command'''
'''----------------------------------------------------------------------------------------------'''
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    
    await update.message.reply_text(text=START_MESSAGE)