import requests
import telegram
from bs4 import BeautifulSoup
from apscheduler.schedulers.blocking import BlockingScheduler

bot = telegram.Bot(token = '1095861554:AAHd-tc6vTtYGqQsNvFgMg_SFjzYGWAQaJM')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0150&date=20200827'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')

def job_function():
    title_list = soup.select('div.info-movie')
    temp = 0
    for i in title_list:
        title_list = i.select_one('a > strong').text.strip()
        if('테넷' in title_list):
            bot.sendMessage(chat_id=1232288185, text = "테넷 예매가 열렸습니다.")
            temp = 1
            sched.pause()

sched = BlockingScheduler()
sched.add_job(job_function, 'interval', seconds=30)
sched.start()

