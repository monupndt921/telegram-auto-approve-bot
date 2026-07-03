import asyncio
from telegram import Update
from telegram.ext import (
    Application,
    ChatJoinRequestHandler,
    ContextTypes,
)

BOT_TOKEN = "8821858157:AAHCDZBqmHtUC1PvJJw4gD4XPQzdRUsGYoU"

async def approve(update: Update, context: ContextTypes.DEFAULT_TYPE):
    try:
        await update.chat_join_request.approve()
        print(f"Approved: {update.chat_join_request.from_user.id}")
    except Exception as e:
        print(e)

async def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(ChatJoinRequestHandler(approve))

    print("Auto Approve Bot Running...")

    await app.initialize()
    await app.start()
    await app.updater.start_polling()

    while True:
        await asyncio.sleep(3600)

if __name__ == "__main__":
    asyncio.run(main())