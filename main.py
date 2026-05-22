from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

TOKEN = 8598100011:AAF53-MTFRPoVeph3rCSz-_WgT44DvwXPpg

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text (سلام؛ به ابرام‌بگو خوش اومدین)

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
await update.message.reply_text(update.message.text)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

app.run_polling()
