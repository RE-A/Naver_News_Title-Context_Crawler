# Naver_News_Title-Context_Crawler v 0.2.0

## NOTICE

이 프로젝트는 현재 개발 중입니다. 꾸준히 버그 수정이나 기능 구현 중이며, 사용하시면서 어떤 오류가 있다면 이슈로 제보해 주시면 감사하겠습니다.

---------------------------------

### 이 프로젝트는

 자연어 처리나 통계 등에 사용할 수 있도록, 네이버 랭킹 뉴스에서 섹션별로 뉴스의 제목 또는 본문을 수집해 주는 프로그램입니다.
 수집된 텍스트들은 엑셀의 형태로 저장됩니다.
 
 [업데이트 로그](https://github.com/RE-A/Naver_News_Title-Context_Crawler/wiki/Update-Note)
 
--------------------------------

### 사용 준비

- 이 프로그램은 python 3.7.3 버젼을 기준으로 개발되었습니다.
 
  이 레포지토리를 clone 하거나, zip 파일로 다운받는 등으로 소스코드를 다운받고, 필요한 라이브러리 설치를 위해 콘솔에 

    pip install -r requirements.txt

를 입력합니다. 실행은 run.py를 통해 실행하며, 
실행시 설정할 수 있는 옵션은 아래에 설명되어 있습니다.

--------------------------------------------------

### 크롤링 옵션

아래의 각 옵션은, 파라미터로 넣을 때 True가 됩니다.
예시로 넣은 사진들은 모두 개발자의 정치적 견해나 성향과는 무관하며, 단순한 예시입니다.


 - -t : title의 약자로, 이 옵션을 넣으면 본문을 크롤링하지 않고 제목만 크롤링합니다. 기본값은 False 입니다.
 - -i : image의 약자로, 이 옵션을 넣으면 사진에 달린 캡션(부가 설명)도 크롤링합니다. 기본값은 False 입니다.
     * 아래 노란색으로 칠한 요소를 캡션으로 부릅니다.
     ![image](https://user-images.githubusercontent.com/11948404/63771510-45d9b280-c912-11e9-839a-a576c205b77f.png)
     
      **주의 : 사진 자체는 크롤링 하지 않습니다.**
      
 - -s : summary의 약자로, 이 옵션을 넣으면 기사의 서두나 중간에 굵은 글씨로 나오는 요약문도 크롤링합니다. 기본값은 False입니다.
    * 아래 노란색으로 칠한 요소를 요약문으로 부릅니다.
![image](https://user-images.githubusercontent.com/11948404/63771414-14f97d80-c912-11e9-85c7-9c050f8957e7.png)
![image](https://user-images.githubusercontent.com/11948404/63771303-e24f8500-c911-11e9-9ff6-c0250cbcd842.png)
 - -l : linefeed의 약자로, 이 옵션을 넣으면 기사 원문의 개행들을 반영합니다. 이 옵션을 넣지 않을시, 
 기사 하나의 본문은 전부 하나의 문단으로 나오며, 기존의 개행 역시 단순한 띄어쓰기 하나로 대체됩니다. 문장을 수집하는 경우에 적합합니다. 기본값은 False 입니다.
 - -d : days의 약자로, 이 옵션은 파라미터를 필요로 합니다. -d {숫자}로 과거의 며칠간의 기사를 수집할 지 결정합니다. 
 예를 들어, **-d 3** 을 입력할 시, 오늘이 26일이었다면 25일, 24일, 23일  3일 간의 기사들을 수집합니다.  기본값은 3입니다.
 - --noinfo : 기본적으로 프로그램 실행 시 현재의 진행 상황을 콘솔에 표시합니다. 이 옵션을 입력하면 프로그램이 종료될 때까지 어떤 메세지도 표시하지 않습니다.
 
    **주의 : 오늘의 기사는 수집하지 않습니다. 새벽 시간대에는 오늘 날짜의 랭킹 뉴스가 아직 없을 가능성이 있기 때문입니다.**

 &nbsp;

#### 사용 예시
  
  콘솔창에서 프로젝트 경로로 이동한 다음, 아래와 같이 파라미터를 입력하면 됩니다.
  
    python run.py -si -d 20
 
 이 옵션은, -s 옵션과 -i 옵션이 활성화 되었으므로, summary와 이미지 캡션을 모두 크롤링하며, 지난 20일간의 기사를 크롤링 하게 됩니다.

 
 **주의 : -t와 -d 옵션을 제외한 나머지 옵션들은, 본문(context)까지 수집할 때만 유효한 옵션들입니다. 
 만약 -t를 파라미터로 넣었다면, -d 옵션을 제외한 나머지 -i,-s,-l 옵션은 사용되지 않습니다.**
 
 &nbsp;
 
 다른 예시는 아래와 같습니다.
 
    python run.py -t --noinfo
 
 이 옵션에서는  -t 옵션이 활성화 되었으므로 제목만 크롤링하고 본문은 크롤링하지 않습니다. 또한 --noinfo 옵션이 활성화 되었으므로, 진행 상황에 관한 어떠한 정보도 출력하지 않습니다.
 
 
 ------------------------------------------------------
 
### 사용 방법

필요한 옵션을 넣고 콘솔창에서 실행하면, 크롤링할 분야 선택에 관한 안내문이 나옵니다. 원하는 분야를 입력하면 자동으로 크롤링을 시작합니다.

* 크롤링된 자료는 모두 Output 폴더에 xlsx 파일 형태로 저장됩니다. 제목만 크롤링하는 옵션(-t)를 적용했을 경우, '내용' 열은 비어있는 상태로 출력됩니다.
* 아래와 같이 "카테고리/날짜/링크/제목/내용"의 형식으로 저장됩니다.


![캡처](https://user-images.githubusercontent.com/11948404/64064599-a2a0da00-cc3e-11e9-92c6-aa32a3589901.PNG)

데이터를 가공하실 때는 엑셀을 이용하면 편리하고, 파이썬에서 불러올 땐 pandas 라이브러리 등을 이용하시면 됩니다.
예를 들어, 뉴스 본문 데이터만 가져오고 싶을 때는 다음과 같은 코드를 이용 할 수 있습니다.

```python
import pandas as pd
df = pd.read_excel('NewsCrawlList.xlsx', sheetname='Sheet1')
# 뉴스 본문 데이터만 불러오기
context_data = df['내용']
```

 
 -------------------------------------------------------
 
### Q&A

1. 네이버 랭킹 뉴스에는 분야별로 뉴스가 30개씩 올라오는데, 크롤링한 뉴스의 개수가 30의 배수가 아닙니다.
   * 네이버 랭킹 뉴스는 일자별로 한번 올라왔던 뉴스가 또 올라올 수 있고, 이 프로그램은 크롤링된 뉴스의 중복을 자동으로 제거하고 있습니다. 따라서 뉴스의 개수가 맞지 않을 수 있습니다.
   
2. 요약문을 크롤하지 않도록 -s 옵션 없이 크롤링을 진행했는데, 몇몇 기사에서는 요약문도 크롤링이 된 것 같습니다.
   * 네이버 뉴스에는 우리가 잘 아는 메이저 언론들을 비롯해, 수백 개의 인터넷 언론들의 기사가 올라옵니다. 언론별로, 심지어 같은 언론에서도 기자분들마다 기사를 작성하는 형식이 달라 요약문 등 몇몇 요소를 거르지 못 하는 경우가 있습니다. 현실적으로 이 모든 경우를 고려하는 프로그램을 작성하는 건 매우 힘든 일입니다. 따라서, **크롤링한 자료를 사용하기 전 데이터를 검수하는 것을 강력히 권장합니다.**
   
----------------------------------------------------------

### 문의

  저는 학생 개발자이며, 어떤 문의나 지원이든 감사히 받고 있습니다. 버그나 기능 건의 등의 모든 문의는 issue를 통해 주시면 감사하겠습니다.
 이 프로그램은 MIT 라이센스를 따르고 있으며, 출처를 남긴다는 전제 하에 코드의 변형이나 이용을 환영합니다.


