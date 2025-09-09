import config
from utils.whitelist import save_whitelist, save_admin_ids
from telegram import Update
from telegram.ext import ContextTypes
from utils.whitelist import admin_only, load_whitelist, load_admin_ids

@admin_only
async def removeuser(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or not context.args[0].isdigit():
        await update.message.reply_text("Usage: /removeuser <user_or_chat_id>")
        return

    remove_id = int(context.args[0])
    whitelist = load_whitelist()
    if remove_id not in whitelist:
        await update.message.reply_text("ID not found in whitelist.")
        return

    whitelist.remove(remove_id)
    save_whitelist(whitelist)
    await update.message.reply_text(f"ID {remove_id} removed from whitelist.")
    
    adminlist = load_admin_ids()
    if remove_id in adminlist:
        adminlist.remove(remove_id)
        save_admin_ids(whitelist)
        await update.message.reply_text(f"ID {remove_id} removed from admin.")
