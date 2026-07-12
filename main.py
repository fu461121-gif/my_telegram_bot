import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters, CallbackQueryHandler

# 🔑 التوكن (فضلاً استبدله بتوكنك الجديد إذا أردت الأمان)
BOT_TOKEN = "8756123739:AAHPbxnTj6sq-dSQaeW-RIy4WJV0_wCt6Uc"

logging.basicConfig(format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
                    level=logging.INFO)

# 1️⃣ أمر /start - القائمة الملونة والمطورة
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🟦 لوحة التحكم", callback_data="dashboard"),
            InlineKeyboardButton("🟩 معلومات البوت", callback_data="about")
        ],
        [
            InlineKeyboardButton("🟨 مساعدة", callback_data="help"),
            InlineKeyboardButton("🟧 تنبيه", callback_data="alert")
        ],
        [
            InlineKeyboardButton("👨‍💻 المطور", url="https://t.me/lllIlIlIlIllIlIlll"),
            InlineKeyboardButton("📤 مشاركة البوت", url="https://t.me/share/url?url=https://t.me/your_bot_username")
        ],
        [
            InlineKeyboardButton("⭐ تابعنا", url="https://t.me/lllIlIlIlIllIlIlll")
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌟 **مرحباً بك في البوت المتطور!**\n\n"
        "اختر من الأزرار الملونة أدناه للتنقل:",
        reply_markup=reply_markup,
        parse_mode="Markdown"
    )

# 2️⃣ أمر /help
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📖 **الأوامر المتاحة:**\n"
        "/start - عرض القائمة الرئيسية\n"
        "/help - عرض هذه الرسالة\n"
        "/about - معلومات البوت\n\n"
        "يمكنك أيضاً استخدام الأزرار الملونة."
    )

# 3️⃣ أمر /about
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 **عن البوت:**\n\n"
        "إصدار 3.0 (متطور)\n"
        "مكتبة: python-telegram-bot\n"
        "منصة: Kuberns\n"
        "مطور: @lllIlIlIlIllIlIlll"
    )

# 4️⃣ معالج الضغط على الأزرار (المطور)
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()  # يزيل الدائرة الزرقاء

    if query.data == "dashboard":
        await query.edit_message_text("📊 **لوحة التحكم:**\n\n✅ البوت يعمل بكفاءة.\n📅 الحالة: نشط.")
    elif query.data == "about":
        await query.edit_message_text("🤖 **معلومات البوت:**\n\nالإصدار 3.0\nتم التحديث بأزرار ملونة.")
    elif query.data == "help":
        await query.edit_message_text("🆘 **المساعدة:**\n\nللتواصل مع المطور، اضغط على زر 'المطور' في الأسفل.")
    elif query.data == "alert":
        await query.edit_message_text("🔔 **تنبيه:**\n\nلا توجد تنبيهات جديدة حالياً.")
    else:
        await query.edit_message_text("❌ زر غير معروف.")

# 5️⃣ الرد على النصوص العادية
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.message.text:
        await update.message.reply_text(f"📩 أنت كتبت: {update.message.text}")

# 6️⃣ تشغيل البوت
def main():
    app = Application.builder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CallbackQueryHandler(button_handler))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, echo))

    print("✅ البوت المتطور يعمل الآن...")
    app.run_polling(allowed_updates=Update.ALL_TYPES)

if __name__ == "__main__":
    main()
    