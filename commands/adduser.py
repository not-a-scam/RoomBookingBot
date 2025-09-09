import config
from utils.whitelist import save_whitelist
from telegram import Update
from telegram.ext import ContextTypes
from utils.whitelist import admin_only

ADMIN_IDS = config.ADMIN_IDS  # Replace with actual admin Telegram user IDs

@admin_only
async def adduser(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("You are not authorized to add users.")
        return

    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /adduser <user_id>")
        return

    new_user_id = int(context.args[0])
    if new_user_id in config.WHITELIST:
        await update.message.reply_text("User is already whitelisted.")
        return

    config.WHITELIST.append(new_user_id)
    save_whitelist(config.WHITELIST)
    await update.message.reply_text(f"User {new_user_id} added to whitelist.")
