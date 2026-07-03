
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

TOKEN = 123456789:AAxxxxxxxxxxxxxxxxxxxxxxxxxxxxx

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "✅ أهلاً بك في بوت إدارة المقهى!\n\n"
        "البوت يعمل بنجاح."
    )

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))

app.run_polling()
