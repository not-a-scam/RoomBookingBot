import sys
sys.path.append("../RoomBookingBot")

import text
import config
from .Booking import Booking
from telegram import Update
from utils.whitelist import whitelist_only
from utils.group import load_group_id
from telegram.ext import (
    ContextTypes, 
    ConversationHandler, 
    CommandHandler, 
    MessageHandler, 
    filters
)

#Conversation States
NAME, PAX, DATE, TIME, PURPOSE, SCREEN, REQUEST = range(7)
    
# for each command, asks for the next piece of info and stores the result in a booking object nested in telegram user_data
@whitelist_only
async def check(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(text.NAME_CHECK_MSG, parse_mode=config.PARSEMODE)
    return NAME

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    nameInput = update.message.text.split('\n')[0]
    context.user_data["checking"] = Booking(name = nameInput)
    await update.message.reply_text(text.PAX_MSG, parse_mode=config.PARSEMODE)
    return PAX

async def pax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["checking"].pax = update.message.text.split('\n')[0]
    await update.message.reply_text(text.DATE_MSG, parse_mode=config.PARSEMODE)
    return DATE

async def date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["checking"].date = update.message.text.split('\n')[0]
    await update.message.reply_text(text.TIME_MSG, parse_mode=config.PARSEMODE)
    return TIME
    
async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["checking"].time = update.message.text.split('\n')[0]
    await update.message.reply_text(text.PURPOSE_MSG, parse_mode=config.PARSEMODE)
    return PURPOSE

async def purpose(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["checking"].purpose = update.message.text.split('\n')[0]
    await update.message.reply_text(text.SCREEN_MSG, parse_mode=config.PARSEMODE)
    return SCREEN

async def screen(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["checking"].screen = update.message.text.split('\n')[0]
    await update.message.reply_text(text.REQUEST_MSG, parse_mode=config.PARSEMODE)
    return REQUEST
    
async def request(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["checking"].request = update.message.text.split('\n')[0]
    await update.message.reply_text(text.CHECKED_MSG + "\n\n" + context.user_data["checking"].__str__(), parse_mode=config.PARSEMODE)
    await context.bot.send_message(chat_id=load_group_id(), text="Room Checking Request: \n\n" + context.user_data["checking"].__str__())
    return ConversationHandler.END
    
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(text.CANCEL_MSG)
    return ConversationHandler.END

conv_handler = ConversationHandler(
        entry_points=[CommandHandler("check", check)],
        states={
            NAME: [MessageHandler(filters.TEXT & (~filters.Text(["/cancel", "/Cancel", "/CANCEL"])), name)],
            PAX: [MessageHandler(filters.TEXT & (~filters.Text(["/cancel", "/Cancel", "/CANCEL"])), pax)],
            DATE: [MessageHandler(filters.TEXT & (~filters.Text(["/cancel", "/Cancel", "/CANCEL"])), date)],
            TIME: [MessageHandler(filters.TEXT & (~filters.Text(["/cancel", "/Cancel", "/CANCEL"])), time)],
            PURPOSE: [MessageHandler(filters.TEXT & (~filters.Text(["/cancel", "/Cancel", "/CANCEL"])), purpose)],
            SCREEN: [MessageHandler(filters.TEXT & (~filters.Text(["/cancel", "/Cancel", "/CANCEL"])), screen)],
            REQUEST: [MessageHandler(filters.TEXT & (~filters.Text(["/cancel", "/Cancel", "/CANCEL"])), request)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )
