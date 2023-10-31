from  requests import get

#获取水余量
def getWater(URL: str):
    waterData = get(URL)    #获取爬虫信息
    returnJson = waterData.json() 
    mainData = returnJson["data"]   #从返回的json中提取数据
    Remain = mainData["balance"]    #从数据中提取余量信息
    return Remain   #返回余量信息

#获取电余量
def getElec(URL: str):
    elecData = get(URL) #获取爬虫信息
    returnJson = elecData.json()
    mainData = returnJson["data"]   #从返回的json中提取数据
    Remain = mainData["balance"]    #从数据中提取余量信息
    return Remain   #返回余量信息