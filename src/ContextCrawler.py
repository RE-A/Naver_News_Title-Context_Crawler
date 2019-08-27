# 뉴스 본문을 크롤링하면서 본문을 정리한다.
# context_crawl이 메인이고 다른 함수들은 이 context_crawl 안에서 작동한다.
# string 수준에서 작동하는 함수는 beautify 뿐이다.

from bs4 import BeautifulSoup
from urllib.request import urlopen
import re


def image_clean(_text_div):
    # 이미지와 그 주석까지 모두 날린다.
    for imgtag in _text_div.find_all('span',{'class':'end_photo_org'}):
        imgtag.extract()
    return _text_div


def summary_clean(_text_div):
    # 보통 기사 서문에 나오는 summary는 두 가지 형태가 있음.
    # 1. <strong class="media_end_summary"> 형태로 지정
    # 2. 단순히 <strong> 태그로 지정
    # 두 가지 방법 모두 strong 태그를 제거하면 모든 요약문을 제거할 수 있음.

    for strong_tag in _text_div.find_all('strong'):
        strong_tag.extract()
    return _text_div


def beautify(plaintext, is_lf_exist):
    plaintext = plaintext.replace('/t', '').replace('[]', '').replace('</div>','')
    tag_cleaner = re.compile('<(.*?)>')
    comment_cleaner = re.compile('<!--.*-->')
    # bold_cleaner = re.compile('<\/?strong>')
    lf_maker = re.compile('(<br/?>)+')
    lf_cleaner = re.compile('(\n){2,}')    # 개행이 여러개일 경우 하나로 줄인다.
    space_cleaner = re.compile('[ ]+')

    plaintext = plaintext.replace('<div class="_article_body_contents" id="articleBodyContents">','')
    plaintext = re.sub(comment_cleaner, '', plaintext)
    plaintext = re.sub(lf_maker, '\n\n', plaintext)
    plaintext = re.sub(tag_cleaner, ' ', plaintext)
    # plaintext = re.sub(bold_cleaner, '', plaintext)
    plaintext = re.sub(lf_cleaner, '\n', plaintext)

    if not is_lf_exist:
        plaintext = re.sub('\r?\n|\r', ' ', plaintext)

    plaintext = re.sub(space_cleaner, ' ', plaintext)

    # 빈 line feed 제거용.
    plaintext = plaintext.strip()
    return plaintext


def text_clean(_text_div, settings):
    for script in _text_div(["script", "style", "a"]):
        script.extract()

    is_image_clean = settings['image']
    is_summary_clean = settings['summary']
    is_lf_exist = settings['lf']

    # cleaner 함수들을 이용해 본문을 정리한다.
    if not is_image_clean:
        _text_div = image_clean(_text_div)
    if not is_summary_clean:
        _text_div = summary_clean(_text_div)

    # 텍스트화 후 정규식을 이용하여 본문을 정리한다.
    text_div = str(_text_div)
    return beautify(text_div, is_lf_exist)




def context_crawl(link_url, settings):
    html = urlopen('http://'+link_url)
    news_page = BeautifulSoup(html, 'html.parser')

    text_div = news_page.find('div',{'id' : 'articleBodyContents' })
    cleaned_text = text_clean(text_div, settings)
    return cleaned_text




if __name__ == "__main__":
    context_crawl('https://news.naver.com/main/ranking/read.nhn?mid=etc&'
                  'sid1=111&rankingType=popular_day&oid=023&aid=0003468929&date=20190822&type=1&rankingSeq=2&rankingSectionId=100')