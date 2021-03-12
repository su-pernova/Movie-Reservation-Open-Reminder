import requests
import telegram
from bs4 import BeautifulSoup

bot = telegram.Bot(token = '1095861554:AAHd-tc6vTtYGqQsNvFgMg_SFjzYGWAQaJM')
url = 'http://www.cgv.co.kr/common/showtimes/iframeTheater.aspx?areacode=01&theatercode=0150&date=20200826'
html = requests.get(url)
soup = BeautifulSoup(html.text, 'html.parser')
print(soup.select_one('a > strong'))
