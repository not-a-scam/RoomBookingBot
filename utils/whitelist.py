import config
from telegram import Update
from telegram.ext import ContextTypes, filters
from functools import reduce
import operator
import json
import os

WHITELIST_FILE = "./data/whitelist.json"
ADMIN_ID_FILE = "./data/admin_id.json"

def load_admin_ids():
    if not os.path.exists(ADMIN_ID_FILE):
        return []
    with open(ADMIN_ID_FILE, "r") as f:
        return json.load(f)

def save_admin_ids(admin_ids):
    with open(ADMIN_ID_FILE, "w") as f:
        json.dump(admin_ids, f)

def load_whitelist():
    if not os.path.exists(WHITELIST_FILE):
        return []
    with open(WHITELIST_FILE, "r") as f:
        return json.load(f)

def save_whitelist(whitelist):
    with open(WHITELIST_FILE, "w") as f:
        json.dump(whitelist, f)

def whitelist_only(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in load_whitelist():
            await update.message.reply_text("Sorry, you are not authorized to use this bot.")
            return
        return await func(update, context, *args, **kwargs)
    return wrapper

def get_whitelist_filter():
    whitelist_filter = reduce(
        operator.or_,
        [filters.User(user_id) for user_id in load_whitelist()]
    )
    return whitelist_filter

def admin_only(func):
    async def wrapper(update: Update, context: ContextTypes.DEFAULT_TYPE, *args, **kwargs):
        user_id = update.effective_user.id
        if user_id not in load_admin_ids():
            await update.message.reply_text("Sorry, you are not authorized to use this command.")
            return
        return await func(update, context, *args, **kwargs)
    return wrapper
