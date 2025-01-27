import DataCrawl
import DataRefine
import DataCrawlByDate
import numpy as np
import CrawlVisual
from ChangeFinder import ChangeFind
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS,ImageColorGenerator
import PIL.Image as pilimg
import os
import matplotlib
matplotlib.use('agg')

def Main(resultKeyword):
    plt.clf() 
    resultData = list()
    refinedInputList = []
    wc = list()
    titleText = list()
    inputKeyword = list()
    inputKeyword.append(resultKeyword[:2])
    inputKeyword.append(resultKeyword[2:])
    
    for i in range(2):
        DataCrawl.SetKeyWord(inputKeyword[i])
        refinedInputList.append(str(inputKeyword[i][0] + ', ' + inputKeyword[i][1])) # 2차 crawl을 위해, 정제 및 저장
        
        crawledData = DataCrawl.GetCrawlingResult()
        refinedData = DataRefine.DataRefining(crawledData)
        resultData.append(refinedData)
    targetDate = ChangeFind(resultData).targetDate

    count = 0
    for i in range(2): # 1 : 클라우드, 2 : 클라우드 보안
        print('[알림]', '\n','-'*60,'\n', refinedInputList[i], '에 대한 상세검색을 진행합니다','\n','-'*60,'\n')
        DataCrawlByDate.query = str(refinedInputList[i]) # input 재활용
        for j in range(2): # 1 : 최상권, 2 : 최하권
            for k in range(2): # 1 : 시작일 - 종료일
                visualInfoList = []
                if j == 0:
                    visualInfoList.append('관심도 상위 구간') # 검색 주제
                else:
                    visualInfoList.append('관심도 하위 구간') # 검색 주제

                directlyCrawledData = DataCrawlByDate.GetNewsCrawlingData(targetDate[count]) # 2nd 크롤링 result
                fileNumber = (count % 4) + 1
                DataCrawlByDate.GetExcelResultQuery(directlyCrawledData, fileNumber)
                
                visualInfoList.append(refinedInputList[i]) # 검색 주제
                visualInfoList.append(targetDate[count]) # 기간(날짜)
                refinedText = DataRefine.DataRefining2(directlyCrawledData, visualInfoList)
                titleText.append(refinedText)
                wc.append(CrawlVisual.WordData(refinedText, count, titleText[count][0]))
                count = count + 1
if __name__ == '__main__':
    # Main(['클라우드', 'cloud', '클라우드 보안', 'cloud security'])
    Main()