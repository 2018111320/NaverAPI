import DataCrawl
import DataRefine
import DataVisual

def Gradient(ratio):
    
    pass

def Main():    
    # 출력할 keyWord 입력 받기 <-----------------   
    refinedData = DataRefine.DataRefining(DataCrawl.GetCrawlingresult)
    DataVisual.PrintInfo(refinedData)

if __name__ == '__main__':
    Main()