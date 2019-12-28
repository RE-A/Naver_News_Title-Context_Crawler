# Written by RE-A
# 네이버 섹션별 랭킹 뉴스 크롤러
import argparse
import logging
import time

from .Config import Config
from .TitleCrawler import title_crawl
from .Data import select_category, make_file, NewsData
from .ContextCrawler import context_crawl

# NewsData 객체들을 저장하는 리스트.
news_data_list = []

def Crawl(config):
    days_list = config.get_days_list()
    settings = config.get_config()
    crawl_logger = logging.getLogger("Crawl")
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(message)s", datefmt="%m-%d  %H:%M:%S")
    categories = select_category()
    if settings['noinfo']:
        crawl_logger.setLevel(logging.WARNING)

    crawl_logger.info("제목 크롤링을 시작합니다.")
    for category in categories:
        for day in days_list:
            # [(제목, 링크) , (제목, 링크), ...] 형식으로 반환됨
            crawled_datas = title_crawl(category, day)

            for crawled_data in crawled_datas:
                news = NewsData()
                news.set_title_crawl_data(crawled_data[0], crawled_data[1], category, day)
                news_data_list.append(news)
    crawl_logger.info("제목 크롤링이 완료되었습니다.")
    if not settings['title']:
        crawl_logger.info("본문 크롤링을 시작합니다.")
        total_length = len(news_data_list)  # 전체 크롤링할 기사 수
        idx = 0
        for news_data in news_data_list:
            url = news_data.link
            news_data.set_context(context_crawl(url, settings))
            time.sleep(0.03)    # 서버 과부하를 방지하기 위한 크롤링 한번 당 대기시간.
            if (total_length % 30 == 0) :
                crawl_logger.info(str(round(idx / total_length*100,2)) + "% 진행")
            idx += 1
    # File화 process
    make_file(news_data_list)
    crawl_logger.info("엑셀 파일 작성이 완료되었습니다. Output 폴더를 확인해주세요.")



# 날짜를 뺄 시 now-datetime.timedelta(days=23) 과 같은 형식 활용할 것.

def main():
    # image, summary, linefeed는 title이 False, 즉 기사 본문들도 크롤링 할때만 유효한 옵션임.
    # title : 제목만 크롤링 할 것인가?
    # image : 이미지의 캡션도 크롤링 할 것인가?(이미지 크롤링은 미구현)
    # summary : 기사 서두나 중간에 굵은 글씨로 나오는 요약문 역시 크롤링 할 것인가?
    # linefeed : 기사의 문단별 개행을 반영할 것인가? 옵션을 넣지 않을 시(False) 개행 없이 문장사이 띄어쓰기만 된 채로 쭉 붙어서 나옴.
    # days : 어제 날짜로부터 몇일치를 크롤링할 것인가?
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--title', required=False, action='store_true', default=False)
    parser.add_argument('-i','--image', required=False, action='store_true', default=False)
    parser.add_argument('-s','--summary', required=False, action='store_true', default=False)
    parser.add_argument('-l','--linefeed', required=False, action='store_true', default=False)
    parser.add_argument('-d','--days', required=False, type=int, default=3)
    parser.add_argument('--noinfo', required=False, action='store_true', default=False)

    args = parser.parse_args()
    config = Config(args.title, args.image, args.summary, args.linefeed, args.days, args.noinfo)

    # Main Procedure
    Crawl(config)

    # print(type(args.title))
    # print(type(args.summary))
    # print(args.image)
    # print(args.linefeed)

if __name__ == "__main__":
    main()




