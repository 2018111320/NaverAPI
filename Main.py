import DataCrawl
import DataRefine
import DataVisual
import DataCrawlByDate

def Main():    
    # 민지 테스트
    data = {
        0:{'date': '2019.03.03.', 'title': 'KT, 멀티 클라우드 전략 확대?…MS와도 손잡는다', 'contents': ' KT가 멀티 클라우드 전략을 확대한다. 지난해 VM웨어와 손을 잡은데 이어 이번엔 마이크로소프트(MS)와 전략적 협업을 추진한다. 다만 KT는 지난 2011년부터 퍼블릭 클라우드 서비스인 ‘유클라우드비즈’를 운영 중인... '},
        1:{'date': '2019.03.03.', 'title': '강원도, 18개 시군과 클라우드 기반 스마트 안전도시 조성', 'contents': ' 강원도가 도내 전역을 대상으로 클라우드 기반 스마트 안전도시를 조성한다. 3일 도에 따르면 전국 최초로 18개 시·군을 통합하는 클라우드 기반 스마트시티 통합플랫폼 구축 사업을 추진한다. 앞서 도와 춘천시는... '},
        2:{'date': '9면 TOP', 'title': "[르포]'클라우드 특화' 더존비즈온 춘천 데이터센터를 가다", 'contents': ' 더존비즈온은 소프트웨어(SW)업계 최초로 춘천에 클라우드 IDC를 만들었다. 2011년에 설립된 춘천IDC는 2015년... 최대 100개 고객을 지원할 수 있는 대용량 메모리 서버로, 퍼블릭 클라우드 2만여 고객을 지원한다.... '},
        3:{'date': '2019.03.03.', 'title': "네이버 클라우드 플랫폼, 빅데이터 분석 솔루션 '펜타호' 등록", 'contents': ' 네이버 클라우드 플랫폼 마켓플레이스에 등록했다. 펜타호는 100% GUI(Graphical User Interface) 환경을 바탕으로... 펜타호가 네이버 클라우드 마켓플레이스에 등록되면서 매달 사용한 만큼 비용으로 지불할 수 있게 됐다.... '},
        4:{'date': '2019.03.03.', 'title': 'AR·VR·클라우드로…5G 시대 중심에 선 게임', 'contents': ' 5G의\xa0빠른\xa0속도,\xa0초저지연\xa0등\xa0강점을\xa0바탕으로\xa0AR·VR(증강·가상현실),\xa0클라우드\xa0게임\xa0등이... 또\xa0이번\xa0MOU를\xa0통해\xa0양사는\xa05G\xa0모바일\xa0게임,\xa0클라우드\xa0게임\xa0서비스\xa0출시\xa0협력은\xa0물론\xa0국제\xa0e스포츠... '},
        5:{'date': '2019.03.03.', 'title': '한국전파진흥협회, ‘클라우드 서비스 개발 전문가’ 국비지원 과정 44명 수료', 'contents': ' 집중육성사업 ’클라우드 서비스 개발 전문가‘ 과정(서울ㆍ아산)을 2018년 9월 17일부터 올해 2월 28일까지 주5일, 830시간 교육과정 44명에 대한 수료식을 실시했다고 3일 밝혔다. 클라우드 서비스 개발 전문가 과정은 4차... '},
        6:{'date': '24면 3단', 'title': "이호스트ICT, 윤커뮤니케이션즈와 업무협약… '클라우드' 서비스 강화", 'contents': ' KT 클라우드 서비스 제공을 위한 공동사업 업무협약을 체결했다고 밝혔다. 이번 협약은 양사 동반성장 및 사업영역 확대를 위해 추진됐다. 이호스트ICT는 클라우드 전용 솔루션과 고객 맞춤형 컨설팅 및... '},
        7:{'date': '2019.03.01.', 'title': '[단독]클라우드 관리 기업 메가존, 480억 투자 받았다', 'contents': ' 국내 클라우드 관리 기업(MSP) 메가존클라우드가 480억원 규모의 투자 유치에 성공했다. 관련 분야 유치 규모로는 역대 최대다. 이번 투자 유치로 메가존은 신사업 등 공격적인 사업 확장에 나설 것으로 예상된다. 1일... '},
        8:{'date': '2019.03.01.', 'title': '50개 행정·공공기관 113개 시스템 클라우드 도입 예정', 'contents': ' 올해 행정·공공기관이 113개 시스템이 클라우드화 되고, 그 중 27개 시스템에는 민간 클라우드가 도입될 것으로 전망된다. 과학기술정보통신부(장관 유영민)는 1일 2019년도 행정·공공기관 클라우드컴퓨팅 수요조사... '},
        9:{'date': '2019.02.28.', 'title': '[기고] 클라우드 시장 개화기는 지금', 'contents': ' 클라우드 업계는 IBM과 같은 기술 기업의 연이은 인수합병과 함께 새로운 표준을 제시하는 기술적 진보가 이루어진 획기적인 해였다. 이러한 기술 업계의 변화에 맞춰, 기업 역시 경쟁력을 고취하는데 적합한 클라우드가... '}
    }
    resultWordData = DataRefine.DataRefining2(data)
    
    # 출력할 keyWord 입력 받기 <-----------------
    resultData = list()
    inputValue = ''
    listForRecycle = []
    
    test = [['클라우드', 'cloud'], ['클라우드 보안', 'cloud security']]
    for i in range(2):
        # inputValue = input('키워드를 2개 입력하세요. (ex. 클라우드, cloud)\n')
        # DataCrawl.SetKeyWord(inputValue.split(','))
        # listForRecycle.append(inputValue)
        DataCrawl.SetKeyWord(test[i])
        listForRecycle.append(str(test[i]))

        crawledData = DataCrawl.GetCrawlingResult()
        refinedData = DataRefine.DataRefining(crawledData)
        resultData.append(refinedData)
    # DataVisual.PrintInfo(refinedData)기존 그래프
    DataVisual.ChangeFind(resultData)

    for i in range(2):
        print('[', listForRecycle[i], '에 대한 상세검색 ]')
        DataCrawlByDate.query = listForRecycle[i] # input 재활용
        directlyCrawledData = DataCrawlByDate.GetNewsCrawlingData() # <------------------- 워드 클라우드용 데이터
        DataCrawlByDate.GetExcelResultQuery(directlyCrawledData)

if __name__ == '__main__':
    Main()