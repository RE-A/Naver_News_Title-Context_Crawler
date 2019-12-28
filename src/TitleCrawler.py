# 기사 제목들을 크롤링하는 라이브러리다.
# 기사 제목과 링크를 반환하며, 링크는 본문을 크롤링할 때 사용된다.

from bs4 import BeautifulSoup
from Data import categories, RANKING_NEWS_URL_FORMAT, get_today
from urllib.request import urlopen


def title_crawl(category, selected_date=get_today()):
    # 해당 카테고리의 그날의 기사들을 모두 크롤링.
    # title_dates : key가 제목, value가 해당 기사 링크
    title_datas = {}
    selected_date = selected_date.replace('-', '')
    html = urlopen(RANKING_NEWS_URL_FORMAT.format(categories.get(category), selected_date))
    ranking_page = BeautifulSoup(html, 'html.parser')

    ranking_headlines = ranking_page.find_all('div', {'class': 'ranking_headline'})
    for ranking_headline in ranking_headlines:
        title_data = ranking_headline.find('a')
        title_datas[title_data['title']] = "news.naver.com" + title_data['href']
    return list(title_datas.items())


if __name__ == "__main__":
    # Example
    title_crawl(category='경제')
