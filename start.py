
import json
import os
import time
from datetime import date
import schedule
import telebot


def main():
    token = "5467137013:AAHZ7dEK5mLlrPMUn-ZzWR2agqPOzvgIcHo"
    #token = os.environ.get("TOKEN")
    bot = telebot.TeleBot(token)
    today = date.today()
    day = today.strftime("%d-%m")
    kun = today.strftime("%d-%m-%Y")
    # path = os.path.abspath(os.getcwd())
    path = os.path.dirname(__file__)
    
    f = open(path+'/staffs.json')
    print(f)
    data=json.load(f)

    for i in data['staffs']:
        if((i["birthday"]).startswith(day)):
            person = (i["name"])
            try:
                print(person)
                print ("Bugun "+day)
                bot.send_photo(-1001712122376, photo=open(path+'/rasm.jpg', 'rb'),caption="πππ*Happy birthday!!!* \n\nπToday is birthday of *{}!* \n Congratulations! πππππ\n\n*Our social networks:* \n[WWW](https://www.siut.uz/index.php) β«οΈ [Instagram](https://www.instagram.com/siut.uz/) β«οΈ [Facebook](https://www.facebook.com/siut.uz) β«οΈ [Telegram](https://t.me/siut_uz)\nΒ©οΈ Copyright: @Islom\_Mamatov".format(person), parse_mode='Markdown')

            except:
                print ("Qandaydir xatolik")
    bot.send_message(-321996347, text="Bot is working properly. System date is: "+kun)            
        
        
        
    f.close()
    


#schedule.every(1).minutes.do(main)
# schedule.every().day.at("02:00").do(main)

# while True:
#     schedule.run_pending()
#     time.sleep(1)


if __name__ == '__main__':
    main()
# Weather forecast
#bot.send_photo(-1001712122376, photo=open('rain.jpg', 'rb'),caption="*Good morning!!!* \n\nToday will rain. π§ Don't Forget Your Umbrella. \n _Have a nice day!_ π\n\n*Our social networks:* \n[WWW](https://www.siut.uz/index.php) β«οΈ [Instagram](https://www.instagram.com/siut.uz/) β«οΈ [Facebook](https://www.facebook.com/siut.uz) β«οΈ [Telegram](https://t.me/siut_uz)\nΒ©οΈ Copyright: @Islom\_Mamatov", parse_mode='Markdown')


# SIUT Team Group id --> -1001712122376
# Testing group id --> -321996347

#@bot.message_handler(commands=['start'])
#def send_message(message):
# bot.send_photo(-1001712122376, photo=open('robot.jpg', 'rb'),caption=
#     "πππ*Hello world!!!* \n\n I am ***SIUT Assistant Bot.*** I'm created by SIUT IT Center!!! \n\n*I can do:* \nβ Remind about the staff birthdays; π \nβ Remind about important days and holidays, etc \n\n _I'm under construction. Hasta la vista, baby. I'll be back π_  \n\n*Our social networks:* \n[WWW](https://www.siut.uz/index.php) β«οΈ [Instagram](https://www.instagram.com/siut.uz/) β«οΈ [Facebook](https://www.facebook.com/siut.uz) β«οΈ [Telegram](https://t.me/siut_uz)\nΒ©οΈ Copyright: @Islom\_Mamatov", parse_mode='Markdown')


#print("Success!!!")
#bot.infinity_polling(skip_pending = True)