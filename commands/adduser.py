import config
from utils.whitelist import save_whitelist
from telegram import Update
from telegram.ext import ContextTypes
from utils.whitelist import admin_only, load_whitelist

@admin_only
async def adduser(update: Update, context: ContextTypes.DEFAULT_TYPE):

    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /adduser <user_id>")
        return

    new_user_id = int(context.args[0])
    whitelist = load_whitelist()
    if new_user_id in whitelist:
        await update.message.reply_text("User is already whitelisted.")
        return

    whitelist.append(new_user_id)
    save_whitelist(whitelist)
    await update.message.reply_text(f"User {new_user_id} added to whitelist.")
