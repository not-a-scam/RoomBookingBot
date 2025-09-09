from utils.group import save_group_id
import config
from telegram import Update
from telegram.ext import ContextTypes
from utils.whitelist import admin_only

@admin_only
async def setgroup(update: Update, context: ContextTypes.DEFAULT_TYPE):

    group_id = update.effective_chat.id
    save_group_id(group_id)
    await update.message.reply_text(f"Group ID set to {group_id} and saved.")
