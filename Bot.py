import telebot

TOKEN = "9265008383:AAEJMpANeUZ18wxsMg2Hfl9v4mjhCLZEY8M"
bot = telebot.TeleBot(TOKEN)

# លុប Webhook ចោលជាមុនសិន ដើម្បីកុំឱ្យមានជម្លោះជាមួយ Polling
try:
  bot.remove_webhook()
except Exception:
  pass

ADMIN_USERNAME = "alexstore_2"
ADMIN_ID = 6514639693

main_menu = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.row("👤 គណនីរបស់ខ្ញុំ", "🎨 កុម្មង់ Logo")
main_menu.row("របៀបប្រើប្រាស់", "📞 ទាក់ទង Admin")


@bot.message_handler(commands=["start"])
def send_welcome(message):
  bot.reply_to(
      message,
      "សួស្តី! សូមស្វាគមន៍មកកាន់ហាងរបស់យើង។\nសូមជ្រើសរើសមឺនុយខាងក្រោម៖",
      reply_markup=main_menu,
  )


@bot.message_handler(commands=["admin"])
def admin_panel(message):
  if message.from_user.id == ADMIN_ID:
    bot.reply_to(message, "👑 **Admin Control Panel**", parse_mode="Markdown")
  else:
    bot.reply_to(message, "⛔️ សូមអភ័យទោស អ្នកមិនមែនជា Admin ទេ!")


@bot.message_handler(func=lambda message: message.text == "👤 គណនីរបស់ខ្ញុំ")
def account_info(message):
  user = message.from_user
  bot.reply_to(
      message,
      f"📋 **គណនីរបស់ខ្ញុំ**\n\n🆔 ID: `{user.id}`\n👤 ឈ្មោះ: {user.full_name}",
      parse_mode="Markdown",
  )


@bot.message_handler(func=lambda message: message.text == "🎨 កុម្មង់ Logo")
def logo_menu(message):
  logo_keyboard = telebot.types.InlineKeyboardMarkup(row_width=1)
  logo_keyboard.add(
      telebot.types.InlineKeyboardButton(
          "🖼 Logo QR - $0.10",
          url=f"https://t.me/{ADMIN_USERNAME}?text=សួស្តី%20ខ្ញុំចង់កុម្មង់ Logo QR តម្លៃ $0.10",
      ),
      telebot.types.InlineKeyboardButton(
          "🖼 Logo PF - $0.05",
          url=f"https://t.me/{ADMIN_USERNAME}?text=សួស្តី%20ខ្ញុំចង់កុម្មង់ Logo PF តម្លៃ $0.05",
      ),
      telebot.types.InlineKeyboardButton(
          "🖼 Logo CH - $0.05",
          url=f"https://t.me/{ADMIN_USERNAME}?text=សួស្តី%20ខ្ញុំចង់កុម្មង់ Logo CH តម្លៃ $0.05",
      ),
  )
  bot.reply_to(message, "👇 សូមជ្រើសរើសប្រភេទ Logo៖", reply_markup=logo_keyboard)


@bot.message_handler(func=lambda message: message.text == "របៀបប្រើប្រាស់")
def how_to_use(message):
  bot.reply_to(
      message,
      "🛠 **របៀបប្រើប្រាស់:**\n១. ចុចកុម្មង់ Logo\n២. ជ្រើសរើសប្រភេទ Logo"
      " (លោតចូលឆាត Admin ស្វ័យប្រវត្តិ)",
      parse_mode="Markdown",
  )


@bot.message_handler(func=lambda message: message.text == "📞 ទាក់ទង Admin")
def contact_admin(message):
  admin_keyboard = telebot.types.InlineKeyboardMarkup()
  admin_keyboard.add(
      telebot.types.InlineKeyboardButton(
          "💬 ឆាតទៅ Admin", url=f"https://t.me/{ADMIN_USERNAME}"
      )
  )
  bot.reply_to(message, "ចុចប៊ូតុងខាងក្រោម:", reply_markup=admin_keyboard)


print("Bot is running...")
bot.infinity_polling()
  
