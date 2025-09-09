import config
from utils.whitelist import load_whitelist, save_whitelist, load_admin_ids, save_admin_ids
from telegram import Update
from telegram.ext import ContextTypes

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args:
        await update.message.reply_text("Usage: /register <password>")
        return

    password = context.args[0]
    user_id = update.effective_user.id

    if password == config.ADMIN_PASSWORD:
        admin_ids = load_admin_ids()
        if user_id in admin_ids:
            await update.message.reply_text("You are already an admin.")
            return
        admin_ids.append(user_id)
        save_admin_ids(admin_ids)
        
        whitelist = load_whitelist()
        if user_id not in whitelist:
            whitelist.append(user_id)
            save_whitelist(whitelist)
        await update.message.reply_text("You are now registered as an admin.")
        return

    if password == config.REGISTER_PASSWORD:
        whitelist = load_whitelist()
        if user_id in whitelist:
            await update.message.reply_text("This user is already registered.")
            return
        whitelist.append(user_id)
        save_whitelist(whitelist)
        await update.message.reply_text("Registration successful! You are now whitelisted.")
        return

    await update.message.reply_text("Incorrect password. Registration failed.")
