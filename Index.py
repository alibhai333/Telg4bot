from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

BOT_TOKEN = "8427808483:AAEY5Z5bKNRJdUVHuGkTUjqiigcYvz90UQk"  # Replace with your actual bot token

CHANNEL_USERNAME = "@peiroocode"
CHANNEL_LINK = "https://t.me/peiroocode"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🚀 Join PeirooCode Channel", url=CHANNEL_LINK)],
        [InlineKeyboardButton("✅ I Joined", callback_data="joined")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Welcome to PeirooCode Bot!\n\n"
        "To access all bot features, please join our Telegram channel:",
        reply_markup=reply_markup
    )

async def joined(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    user = query.from_user
    await query.answer()

    try:
        member = await context.bot.get_chat_member(CHANNEL_USERNAME, user.id)
        if member.status in ["member", "administrator", "creator"]:
            await query.edit_message_text("✅ Thank you! You now have full access to the bot.")
        else:
            await query.edit_message_text("❌ You must join our channel first.")
    except Exception as e:
        await query.edit_message_text(f"⚠️ Error checking membership: {e}")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
