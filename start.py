
import telebot
import json
#import db
from datetime import date

token = '5467137013:AAHZ7dEK5mLlrPMUn-ZzWR2agqPOzvgIcHo'
bot = telebot.TeleBot(token)

# iconlar uchun link   https://emojipedia.org

today = date.today()
day = today.strftime("%d-%m")
kun = today.strftime("%d-%m-%Y")
print (day)

f = open('staffs.json')
data=json.load(f)

for i in data['staffs']:
    if((i["birthday"]).startswith(day)):
        person = (i["name"])
try:
    print(person)
    bot.send_photo(-321996347, photo=open('rasm.jpg', 'rb'),caption="🎉🎉🎉*Happy birthday!!!* \n\n🎂Today is birthday of *{}!* \n Congratulations! \n\n*Our social networks:* \n[WWW](https://www.siut.uz/index.php) ▫️ [Instagram](https://www.instagram.com/siut.uz/) ▫️ [Facebook](https://www.facebook.com/siut.uz) ▫️ [Telegram](https://t.me/siut_uz)\n©️ Copyright: @Islom\_Mamatov".format(person), parse_mode='Markdown')

except:
    print ("Today nobody's birthday")

f.close()


# SIUT Team Group id is --> -1001712122376

#@bot.message_handler(commands=['start'])
#def send_message(message):
# bot.send_photo(-1001712122376, photo=open('robot.jpg', 'rb'),caption=
#     "🎉🎉🎉*Hello world!!!* \n\n I am ***SIUT Assistant Bot.*** I'm created by SIUT IT Center!!! \n\n*I can do:* \n✅ Remind about the staff birthdays; 🎂 \n✅ Remind about important days and holidays, etc \n\n _I'm under construction. Hasta la vista, baby. I'll be back 👍_  \n\n*Our social networks:* \n[WWW](https://www.siut.uz/index.php) ▫️ [Instagram](https://www.instagram.com/siut.uz/) ▫️ [Facebook](https://www.facebook.com/siut.uz) ▫️ [Telegram](https://t.me/siut_uz)\n©️ Copyright: @Islom\_Mamatov", parse_mode='Markdown')




print("Success!!!")
#bot.infinity_polling(skip_pending = True)