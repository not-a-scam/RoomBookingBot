from utils.group import save_group_id
import config
from telegram import Update
from telegram.ext import ContextTypes
from utils.whitelist import admin_only

ADMIN_IDS = config.ADMIN_IDS  # Replace with your admin IDs

@admin_only
async def setgroup(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    if user_id not in ADMIN_IDS:
        await update.message.reply_text("You are not authorized to set the group.")
        return

    group_id = update.effective_chat.id
    save_group_id(group_id)
    config.update_group_id()
    await update.message.reply_text(f"Group ID set to {group_id} and saved.")
