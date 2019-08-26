# 각종 const 데이터 및 파일화 관련 자잘한 기능 수행하는 파일.
import datetime
import os
import pandas
from pandas import ExcelWriter
from pandas import ExcelFile

RANKING_NEWS_URL_FORMAT = "https://news.naver.com/main/ranking/popularDay.nhn?rankingType=popular_day&sectionId={0}&date={1}"
ROOT_URL = os.path.dirname(os.path.dirname(__file__))

categories = {'정치': 100,
              '경제': 101,
              '사회': 102,
              '생활': 103,
              '세계': 104,
              'IT': 105,
              }


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
        
        입력:    
        """)

        categories = select_categories.split()
        is_categories_valid = True
        for category in categories:
            if not category in categories:
                print(category + " 은(는) 잘못된 값입니다. 다시 입력해주세요.")
                is_categories_valid = False
                break
        if is_categories_valid is True:
            break
    return categories

def make_file(title_data, context_data):
    if not context_data:
        df = pandas.DataFrame({"title" : title_data})
        writer = ExcelWriter(os.path.join(ROOT_URL,'Output','TitleList.xlsx'))
        df.to_excel(writer, 'Sheet1')
        try:
            writer.save()
        except PermissionError:
            print("파일 저장에 실패했습니다. 혹시 TitleList.xlsx이 열려 있나 확인해주세요.")
    else:
        total_data = dict(zip(title_data, context_data))
        df = pandas.DataFrame.from_dict(total_data, orient='index')
        writer = ExcelWriter(os.path.join(ROOT_URL,'Output','NewsCrawlList.xlsx'))
        df.to_excel(writer, 'Sheet1')
        try:
            writer.save()
        except PermissionError:
            print("파일 저장에 실패했습니다. 혹시 NewsCrawlList.xlsx이 열려 있나 확인해주세요.")