import telegram

bot = telegram.Bot(token = '1095861554:AAHd-tc6vTtYGqQsNvFgMg_SFjzYGWAQaJM')

#for i in bot.getUpdates():
#    print(i.message)

bot.sendMessage(chat_id=1232288185, text = "테스트입니다.")
