from google import genai
import telebot

AI_API_KEY="AIzaSyCoQ26OZI0OaDSB9PWszk0sRfmhrdFT3wI"
BOT_TOKEN="8250743200:AAGwrl7j8hZI3qSXr2KZWMlgLQsE4LDdRGQ"

client = genai.Client(api_key=AI_API_KEY)
bot = telebot.TeleBot(BOT_TOKEN)

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.reply_to(message, "salom, Aniphexning AI botiga xush kelibsiz!")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    try:
        response = client.models.generate_content(
            model="gemini-2.0-flash",
            contents=message.text
        )

        if response.text:
            text = response.text.strip()
        else:
            text = "Javob topilmadi."

        bot.reply_to(message, text)

    except Exception as e:
        bot.reply_to(message, f"xatolik yuz berdi: {e}")

print("Dastur ishga tushdi")
bot.polling(none_stop=True)