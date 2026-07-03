import os
from telegram import Update
from telegram.ext import (
    Application,
    ChatJoinRequestHandler,
    ContextTypes,
)

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.chat_join_request.approve()
        print(f"Approved: {update.chat_join_request.from_user.id}")
    except Exception as e:
        print(e)

app = Application.builder().token(BOT_TOKEN).build()

app.add_handler(ChatJoinRequestHandler(approve))

print("Auto Approve Bot Running...")
app.run_polling()