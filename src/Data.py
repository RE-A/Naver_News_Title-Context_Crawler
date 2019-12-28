# 각종 const 데이터 및 파일화 관련 자잘한 기능 수행하는 파일.
import datetime
import os
import pandas
from pandas import ExcelWriter

RANKING_NEWS_URL_FORMAT = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId={0}&date={1}"
ROOT_URL = os.path.dirname(os.path.dirname(__file__))

categories = {'정치': 100,
              '경제': 101,
              '사회': 102,
              '생활': 103,
              '세계': 104,
              'IT': 105,
              }


class NewsData:
    # 항목 추가할 시 make_file 함수 역시 손봐야함.
    def __init__(self):
        self.title = ''
        self.category = ''
        self.link = ''
        self.date = ''
        self.context = ''

    def set_title_crawl_data(self, title, link, category, date):
        self.title = title
        self.category = category
        self.link = link
        self.date = date

    def set_context(self, context):
        self.context = context

    def get_data(self):
        return [self.category, self.date, self.link, self.title, self.context]


def get_today():
    # '2019-01-01' 과 같은 형식의 문자열 날짜 반환
    now = datetime.date.today()
    return now.isoformat()


def select_category():
    while True:
        select_categories = input("""
        크롤링 할 수 있는 다음과 같습니다.
        ------------------------------------------------------------
        '정치' , '경제', '사회' , '생활/문화', '세계', 'IT/과학'
        ------------------------------------------------------------
        크롤링 할 분야를 최소 한가지 이상 선택하여 입력해 주세요. 띄어쓰기로 구분합니다.
        이름이 긴 분야는 앞의 단어만 입력해 주세요.
        ------------------------------------------------------------
        다음 중에서 입력 : '정치', '경제' , '사회' , '생활' , '세계', 'IT'
        EX) 정치 경제
            사회 생활 IT
            경제 사회 생활 세계 IT 정치
        
        입력:""")

        input_categories = select_categories.split()
        is_categories_valid = True
        for category in input_categories:
            if not category in categories:
                print(category + " 은(는) 잘못된 값입니다. 다시 입력해주세요.")
                is_categories_valid = False
                break
        if is_categories_valid is True:
            break
    return input_categories


def make_file(data_list):
    # 엑셀 파일로 출력한다.
    # dataframe을 계속 추가하는 것보단 column 별로 리스트를 만들어서 한번에 dataframe으로 만드는 게 좋은 것 같음.
    crawled_data = [[data.category, data.date, 'http://'+data.link, data.title, data.context] for data in data_list]

    df = pandas.DataFrame(crawled_data)
    df.index = df.index + 1
    df.columns = ['카테고리', '날짜', '링크', '제목', '내용']
    path = os.path.join(ROOT_URL, 'Output', datetime.datetime.now().strftime('%y%m%d_%H_%M_%S') + '_NewsCrawlList.xlsx')
    writer = ExcelWriter(path)
    df.to_excel(writer, 'Sheet1')
    try:
        writer.save()
    except PermissionError:
        print("NewsCrawlList.xlsx가 이미 열려 있습니다. 현재 시간을 제목으로 한 파일이 저장됩니다.")
        alter_path = os.path.join(ROOT_URL, 'Output', datetime.datetime.now().strftime('%y%m%d_%H_%M_%S') + '_NewsCrawlList_2.xlsx')
        writer = ExcelWriter(alter_path)
        df.to_excel(writer, 'Sheet1')
        writer.save()


if __name__ == "__main__":
    # Dataframe making test
    make_file([])