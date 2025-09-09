import config
from utils.whitelist import load_whitelist, save_whitelist
from telegram import Update
from telegram.ext import ContextTypes

async def register(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if not context.args or context.args[0] != config.REGISTER_PASSWORD:
        await update.message.reply_text("Incorrect password. Registration failed.")
        return

    user_id = update.effective_user.id
    whitelist = config.WHITELIST
    if user_id in whitelist:
        await update.message.reply_text("This user is already registered.")
        return

    whitelist.append(user_id)
    save_whitelist(whitelist)
    config.update_whitelist()
    await update.message.reply_text("Registration successful! You are now whitelisted.")
