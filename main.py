import getData
from requests import get
import sched
import time
from json import load
from os import path

#获取当前文件路径，转换为相对路径，并为配置文件路径赋值
dirPath = path.dirname(path.abspath(__file__))
filePath = path.join(dirPath, "Config.json")

#读取配置文件
with open(filePath,'r') as fr: 
	Configs = load(fr) 

def main():
    waterRemain = getData.getWater(Configs["waterURL"])
    elecRemain = getData.getElec(Configs["elecURL"])
    pass

sche.every().day.at("09:00").do(main)

while True:
    sche.run_pending()
    time.sleep(1)

