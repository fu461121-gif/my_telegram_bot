import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

# التوكن (يمكنك وضعه مباشرة أو من البيئة)
BOT_TOKEN = "8756123739:AAHPbxnTj6sq-dSQaeW-RIy4WJV0_wCt6Uc"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🟦 القائمة الرئيسية", callback_data="menu"),
            InlineKeyboardButton("🟥 مساعدة", callback_data="help")
        ],
        [
            InlineKeyboardButton("🟩 عن البوت", callback_data="about"),
            InlineKeyboardButton("👨‍💻 المطور", url="https://t.me/lllIlIlIlIllIlIlll")
        ],
        [
            InlineKeyboardButton("🎨 ألوان", callback_data="colors"),
            InlineKeyboardButton("📱 تواصل", url="https://t.me/lllIlIlIlIllIlIlll")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌟 أهلاً بك في البوت الملون!\n\nاختر من الأزرار الملونة أدناه:",
        reply_markup=reply_markup
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 **قائمة الأوامر:**\n/start - القائمة الرئيسية\n/help - هذه الرسالة\n/about - معلومات البوت\n\nاستخدم الأزرار الملونة للتنقل."
    )

async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 بوت تجريبي ملون\nتم تطويره باستخدام Python\nيعمل على Kuberns\nنسخة 2.1"
    )

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    if query.data == "menu":
        await query.edit_message_text("📋 القائمة الرئيسية - اختر خياراً.")
    elif query.data == "help":
        await query.edit_message_text("🆘 للمساعدة، اكتب /help أو تواصل مع المطور.")
    elif query.data == "about":
        await query.edit_message_text("ℹ️ بوت ملون بتقنية الأزرار التفاعلية.")
    elif query.data == "colors":
        await query.edit_message_text("🎨 هذه أزرار ملونة مع أيقونات:\n🟦 أزرق\n🟥 أحمر\n🟩 أخضر")
    else:
        await query.edit_message_text("❌ زر غير معروف.")

async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        await update.message.reply_text(f"📩 أنت كتبت: {update.message.text}")

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))
    print("✅ البوت الملون شغال...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()