import config
from utils.whitelist import save_whitelist
from telegram import Update
from telegram.ext import ContextTypes
from utils.whitelist import admin_only

ADMIN_IDS = config.ADMIN_IDS  # Replace with actual admin Telegram user IDs

@admin_only
async def removeuser(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("You are not authorized to remove users.")
        return

    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /removeuser <user_or_chat_id>")
        return

    remove_id = int(context.args[0])
    whitelist = config.WHITELIST
    if remove_id not in whitelist:
        await update.message.reply_text("ID not found in whitelist.")
        return

    whitelist.remove(remove_id)
    save_whitelist(whitelist)
    config.update_whitelist()
    await update.message.reply_text(f"ID {remove_id} removed from whitelist.")
