import sys
sys.path.append("../RoomBookingBot")

import text
import config
from telegram import Update
from telegram.ext import (
    ContextTypes, 
    ConversationHandler, 
    CommandHandler, 
    MessageHandler, 
    filters
)

#Conversation States
NAME, PAX, DATE, TIME, PURPOSE, REQUEST = range(6)

class Booking:
    def __init__(
            self = None, 
            name= None, 
            pax= None, 
            date= None, 
            time= None, 
            purpose= None, 
            request= None):
        self.name = name
        self.pax = pax
        self.date = date
        self.time = time
        self.purpose = purpose
        self.request = request
    
    def __str__(self):
        res = ""
        if self.name : res += ("Name: " + self.name + '\n')
        if self.pax : res += ("Number of people: " + self.pax + '\n')
        if self.date : res += ("Date: " + self.date + '\n')
        if self.time : res += ("Time: " + self.time + '\n')
        if self.purpose : res += ("Purpose: " + self.purpose + '\n')
        if self.request : res += ("Requests: " + self.request + '\n')
        if res == "" : res = "Empty"
        return res
    
# for each command, asks for the next piece of info and stores the result in a booking object nested in telegram user_data
async def book(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(text.BOOKING_MSG)
    return NAME

async def name(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    nameInput = update.message.text.split('\n')[0]
    context.user_data["booking"] = Booking(name = nameInput)
    await update.message.reply_text(text.NAME_MSG)
    return PAX

async def pax(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["booking"].pax = update.message.text.split('\n')[0]
    await update.message.reply_text(text.PAX_MSG)
    return DATE

async def date(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["booking"].date = update.message.text.split('\n')[0]
    await update.message.reply_text(text.DATE_MSG)
    return TIME
    
async def time(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["booking"].time = update.message.text.split('\n')[0]
    await update.message.reply_text(text.TIME_MSG)
    return PURPOSE

async def purpose(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["booking"].purpose = update.message.text.split('\n')[0]
    await update.message.reply_text(text.PURPOSE_MSG)
    return REQUEST
    
async def request(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    context.user_data["booking"].request = update.message.text.split('\n')[0]
    await update.message.reply_text(text.REQUEST_MSG + "\n\n" + context.user_data["booking"].__str__())
    await context.bot.send_message(chat_id=config.RBC_GRP_ID, text="Room Booking Request: \n\n" + context.user_data["booking"].__str__())
    return ConversationHandler.END
    
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(text.CANCEL_MSG)
    return ConversationHandler.END

conv_handler = ConversationHandler(
        entry_points=[CommandHandler("book", book)],
        states={
            NAME: [MessageHandler(filters.TEXT, name)],
            PAX: [MessageHandler(filters.TEXT, pax)],
            DATE: [MessageHandler(filters.TEXT, date)],
            TIME: [MessageHandler(filters.TEXT, time)],
            PURPOSE: [MessageHandler(filters.TEXT, purpose)],
            REQUEST: [MessageHandler(filters.TEXT, request)],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
    )