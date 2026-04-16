from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
OWNER_NAME = os.getenv("OWNER_NAME")

async def ping(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("🏓 Pong!")

async def alive(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(f"✅ Bot Alive\n👑 Owner: {OWNER_NAME}")

app = ApplicationBuilder().token(BOT_TOKEN).build()

app.add_handler(CommandHandler("ping", ping))
app.add_handler(CommandHandler("alive", alive))

print("Bot Started 🔥")
app.run_polling()
