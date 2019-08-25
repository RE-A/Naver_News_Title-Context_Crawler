# Written by RE-A
# 네이버 섹션별 랭킹 뉴스 크롤러
import argparse
from Config import Config
from TitleCrawler import title_crawl
from Data import select_category, make_file

def Crawl(config):
    # crawl_data = {title : link} 형태의 dictionary
    # title_data = title
    # context_data = context (본문 내용까지 크롤링 할 시)
    crawl_data = {}
    context_data = []


    categories = select_category()
    print("값을 정상적으로 인식했습니다.")
    days_list = config.get_days_list()
    for category in categories:
        for day in days_list:
            crawl_data.update(title_crawl(category, day))
    # contextcrawl
    # File화 process
    make_file(list(crawl_data.keys()), context_data)



# 날짜를 뺄 시 now-datetime.timedelta(days=23) 과 같은 형식 활용할 것.

def main():
    # 아래의 모든 내용은 title이 False, 즉 기사 본문들도 크롤링 할때만 유효한 옵션임.
    # title : 제목만 크롤링 할 것인가?
    # image : 이미지의 캡션도 크롤링 할 것인가?(이미지 크롤링은 미구현)
    # summary : 기사 서두나 중간에 굵은 글씨로 나오는 요약문 역시 크롤링 할 것인가?
    # linefeed : 기사의 문단별 개행을 반영할 것인가? False 지정시 개행 없이 문장사이 띄어쓰기만 된 채로 쭉 붙어서 나옴.
    # days : 어제 날짜로부터 몇일치를 크롤링할 것인가?
    parser = argparse.ArgumentParser()
    parser.add_argument('-t', '--title', required=False, action='store_true', default=True)
    parser.add_argument('-i','--image', required=False, action='store_true', default=False)
    parser.add_argument('-s','--summary', required=False, action='store_true', default=False)
    parser.add_argument('-l','--linefeed', required=False, action='store_true', default=False)
    parser.add_argument('-d','--days', required=False, default=3)

    args = parser.parse_args()

    config = Config(args.title, args.image, args.summary, args.linefeed, args.days)

    Crawl(config)

    # print(type(args.title))
    # print(type(args.summary))
    # print(args.image)
    # print(args.linefeed)

main()




