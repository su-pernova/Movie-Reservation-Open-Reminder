# 파이썬으로 영화 예매 오픈 알리미 만들기
파이썬으로 영화 예매 오픈 알리미 만들기(텔레그램)

1) movie_crawling.py

영화 예매 사이트를 크롤링하여 필요한 정보를 읽어오느 코드이다.
내가 설정한 영화의 예매가 영화 예매 사이트에서 오픈 되었는지 확인하기 위해 필요하다.

2) crawling_first.py

movie_crawling.py의 코드를 포함하고 있으며,
일정한 초 단위의 간격으로 movie_crawling.py의 코드부분을 반복실행하여
영화 예매가 오픈이 되었는지를 지속적으로 확인할 수 있게 하는 기능을 추가적으로 포함하고 있다.

3) telegram_bot.py

텔레그램 봇을 생성하고 봇이 정상적으로 작동하는지 확인할 수 있는 코드이다.


2번으 코드를 서버 상에서 지속적으로 돌리기 위해, AWS 서버 프로그램을 사용했다(첫 회원가입 무료체험).
