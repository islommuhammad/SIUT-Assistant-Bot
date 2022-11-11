
import json
import os
import time
from datetime import date
import schedule
import telebot


def main():
    token = os.environ.get("TOKEN")
    bot = telebot.TeleBot(token)
    today = date.today()
    day = today.strftime("%d-%m")
    kun = today.strftime("%d-%m-%Y")
    day = "03-11"
    print (day)

    f = open('staffs.json')
    data=json.load(f)

    for i in data['staffs']:
        if((i["birthday"]).startswith(day)):
            person = (i["name"])
            try:
                print(person)
                print ("Bugun"+day)
                bot.send_photo(-321996347, photo=open('rasm.jpg', 'rb'),caption="🎉🎉🎉*Happy birthday!!!* \n\n🎂Today is birthday of *{}!* \n Congratulations! 👏👏👏👏👏\n\n*Our social networks:* \n[WWW](https://www.siut.uz/index.php) ▫️ [Instagram](https://www.instagram.com/siut.uz/) ▫️ [Facebook](https://www.facebook.com/siut.uz) ▫️ [Telegram](https://t.me/siut_uz)\n©️ Copyright: @Islom\_Mamatov".format(person), parse_mode='Markdown')

            except:
                print ("Qandaydir xatolik")
    bot.send_message(-321996347, text="Bot is working properly. System date is: "+kun)            
        
        
        
    f.close()
    


#schedule.every(1).minutes.do(main)
schedule.every().day.at("08:11").do(main)

while True:
    schedule.run_pending()
    time.sleep(1)

if __name__ == '__main__':
    main()
# Weather forecast
#bot.send_photo(-1001712122376, photo=open('rain.jpg', 'rb'),caption="*Good morning!!!* \n\nToday will rain. 🌧 Don't Forget Your Umbrella. \n _Have a nice day!_ 😍\n\n*Our social networks:* \n[WWW](https://www.siut.uz/index.php) ▫️ [Instagram](https://www.instagram.com/siut.uz/) ▫️ [Facebook](https://www.facebook.com/siut.uz) ▫️ [Telegram](https://t.me/siut_uz)\n©️ Copyright: @Islom\_Mamatov", parse_mode='Markdown')


# SIUT Team Group id --> -1001712122376
# Testing group id --> -321996347

#@bot.message_handler(commands=['start'])
#def send_message(message):
# bot.send_photo(-1001712122376, photo=open('robot.jpg', 'rb'),caption=
#     "🎉🎉🎉*Hello world!!!* \n\n I am ***SIUT Assistant Bot.*** I'm created by SIUT IT Center!!! \n\n*I can do:* \n✅ Remind about the staff birthdays; 🎂 \n✅ Remind about important days and holidays, etc \n\n _I'm under construction. Hasta la vista, baby. I'll be back 👍_  \n\n*Our social networks:* \n[WWW](https://www.siut.uz/index.php) ▫️ [Instagram](https://www.instagram.com/siut.uz/) ▫️ [Facebook](https://www.facebook.com/siut.uz) ▫️ [Telegram](https://t.me/siut_uz)\n©️ Copyright: @Islom\_Mamatov", parse_mode='Markdown')


#print("Success!!!")
#bot.infinity_polling(skip_pending = True)