import getData
import time
from json import load
from os import path
import dataProcess
import  alert
import datetime

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#获取当前文件路径，转换为相对路径，并为配置文件路径赋值
dirPath = path.dirname(path.abspath(__file__))
filePath = path.join(dirPath, "Config.json")

#读取配置文件
with open(filePath,'r') as fr: 
	Configs = load(fr)

def dailyReport():
    print(timestamp, " ", "Daily Report start.")
    print(timestamp, " ", "Getting data from server.")
    waterRemain = float(getData.getWater(Configs["waterURL"]))
    elecRemain = float(getData.getElec(Configs["elecURL"]))
    print(timestamp, " ", "Water: ", waterRemain, " Elec: ", elecRemain)
    print(timestamp, " ", "Getting latest record.")
    latestWater =float(dataProcess.getLatestRecord("water")[1])
    latestElec = float(dataProcess.getLatestRecord("elec")[1])
    print(timestamp, " ", "Checking data...")
    if  waterRemain <= 3:
        alertContent = "当前水表余量" + str(waterRemain) + "吨，已不足3吨，请及时充值。（点击跳转）"
        alert.sendAlert(alertContent , "水表余量不足3吨" , "water")
        print(timestamp, " ", "Water Alert sent.")
    else:
        DValue = latestWater - waterRemain
        NotifyContent = "当前水表剩余" + str(waterRemain) + "吨，相比昨日少了"+ str(DValue) + "吨。"
        alert.sendNotify(NotifyContent, "水表每日汇报", "water")
        print(timestamp, " ", "Water Notify sent.")
    time.sleep(2)
    if  elecRemain <= 25:
        alertContent = "当前电表余量" + str(elecRemain) + "kWh，已不足kWh，请及时充值。（点击跳转）"
        alert.sendAlert(alertContent , "电表余量不足25kWh" , "elec")
        print(timestamp, " ", "Elec Alert sent.")
    else:
        DValue = latestElec - elecRemain
        NotifyContent = "当前电表剩余" + str(elecRemain) + "kWh，相比昨日少了"+ str(DValue) + "kWh。"
        alert.sendNotify(NotifyContent, "电表每日汇报", "elec")
        print(timestamp, " ", "Elec Notify sent.")
    print(timestamp, " ", "Saving data to local...")
    dataProcess.addData(waterRemain, elecRemain)
    dataProcess.addDetailData(waterRemain, elecRemain)
    print(timestamp, " ", "Daily Report complete.")
    
def queryHourly():
    print(timestamp, " ", "Getting data from server.")
    waterRemain = float(getData.getWater(Configs["waterURL"]))
    elecRemain = float(getData.getElec(Configs["elecURL"]))
    print(timestamp, " ", "Water: ", waterRemain, " Elec: ", elecRemain)
    dataProcess.addDetailData(waterRemain, elecRemain)
    print(timestamp, " ", "Detailed data saved.")
    
def Report():
    print(timestamp, " ", "Report start.")
    print(timestamp, " ", "Getting data from server.")
    waterRemain = float(getData.getWater(Configs["waterURL"]))
    elecRemain = float(getData.getElec(Configs["elecURL"]))
    print(timestamp, " ", "Water: ", waterRemain, " Elec: ", elecRemain)
    print(timestamp, " ", "Getting latest record.")
    latestWater =float(dataProcess.getLatestRecord("water")[1])
    latestElec = float(dataProcess.getLatestRecord("elec")[1])
    print(timestamp, " ", "Checking data...")
    if  waterRemain <= 3:
        alertContent = "当前水表余量" + str(waterRemain) + "吨，已不足3吨，请及时充值。（点击跳转）"
        alert.sendAlert(alertContent , "水表余量不足3吨" , "water")
        print(timestamp, " ", "Water Alert sent.")
    else:
        DValue = latestWater - waterRemain
        NotifyContent = "当前水表剩余" + str(waterRemain) + "吨，相比昨日少了"+ str(DValue) + "吨。"
        alert.sendNotify(NotifyContent, "水表每日汇报", "water")
        print(timestamp, " ", "Water Notify sent.")
    time.sleep(2)
    if  elecRemain <= 25:
        alertContent = "当前电表余量" + str(elecRemain) + "kWh，已不足kWh，请及时充值。（点击跳转）"
        alert.sendAlert(alertContent , "电表余量不足25kWh" , "elec")
        print(timestamp, " ", "Elec Alert sent.")
    else:
        DValue = latestElec - elecRemain
        NotifyContent = "当前电表剩余" + str(elecRemain) + "kWh，相比昨日少了"+ str(DValue) + "kWh。"
        alert.sendNotify(NotifyContent, "电表每日汇报", "elec")
        print(timestamp, " ", "Elec Notify sent.")
    print(timestamp, " ", "Saving data to local...")
    dataProcess.addData(waterRemain, elecRemain)
    dataProcess.addDetailData(waterRemain, elecRemain)
    print(timestamp, " ", "Report complete.")
