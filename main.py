import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

# قراءة التوكن من متغيرات البيئة (آمن)
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

if not BOT_TOKEN:
    raise ValueError("❌ التوكن غير موجود! تأكد من تعيين TELEGRAM_BOT_TOKEN في متغيرات البيئة.")

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

# 1️⃣ دالة الرد على أمر /start (ترسل أزرار)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("📋 القائمة الرئيسية", callback_data="menu"),
            InlineKeyboardButton("🆘 مساعدة", callback_data="help")
        ],
        [
            InlineKeyboardButton("ℹ️ عن البوت", callback_data="about"),
            InlineKeyboardButton("📱 المطور", url="https://t.me/fu461121")  # غير الرابط لاسمك
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "👋 أهلاً بك في البوت المطور!\n\n"
        "اختر أحد الخيارات من الأزرار أدناه:",
        reply_markup=reply_markup
    )

# 2️⃣ دالة الرد على أمر /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 **قائمة الأوامر المتاحة:**\n\n"
        "/start - عرض الأزرار الرئيسية\n"
        "/help - عرض هذه الرسالة\n"
        "/about - معلومات عن البوت\n\n"
        "يمكنك أيضاً الضغط على الأزرار التفاعلية."
    )

# 3️⃣ دالة الرد على أمر /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 **عن البوت:**\n\n"
        "تم تطوير هذا البوت باستخدام Python ومكتبة python-telegram-bot.\n"
        "يعمل على منصة Kuberns ويستخدم متغيرات البيئة لحماية التوكن.\n\n"
        "🚀 تم إنشاؤه خصيصاً لتجربة الأزرار التفاعلية."
    )

# 4️⃣ دالة معالجة الضغط على الأزرار (CallbackQuery)
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # لإزالة الدائرة الزرقاء التي تظهر بعد الضغط

    if query.data == "menu":
        await query.edit_message_text("📋 هذه هي القائمة الرئيسية.\nيمكنك اختيار ما تريد.")
    elif query.data == "help":
        await query.edit_message_text("🆘 للمساعدة، يمكنك كتابة /help أو التواصل مع المطور.")
    elif query.data == "about":
        await query.edit_message_text("ℹ️ هذا بوت تجريبي يعمل بأحدث التقنيات.\nالنسخة 2.0")
    else:
        await query.edit_message_text("❌ زر غير معروف.")

# 5️⃣ الرد على النصوص العادية (صدى)
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        await update.message.reply_text(f"أنت كتبت: {update.message.text}")

# 6️⃣ تشغيل البوت
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    # إضافة الأوامر
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))

    # إضافة معالج الضغط على الأزرار
    app.add_handler(CallbackQueryHandler(button_handler))

    # إضافة معالج النصوص (الصدى)
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ البوت شغال الآن مع الأزرار الجديدة...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()