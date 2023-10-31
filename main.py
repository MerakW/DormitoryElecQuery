import getData
import sched
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
    

def main():
    waterRemain = float(getData.getWater(Configs["waterURL"]))
    elecRemain = float(getData.getElec(Configs["elecURL"]))
    latestWater =float(dataProcess.getLatestRecord("water")[1])
    latestElec = float(dataProcess.getLatestRecord("elec")[1])
    if  waterRemain <= 3:
        alertContent = "当前水表余量" + str(waterRemain) + "吨，已不足3吨，请及时充值。（点击跳转）"
        alert.sendAlert(alertContent , "水表余量不足3吨" , "water")
    else:
        DValue = latestWater - waterRemain
        NotifyContent = "当前水表剩余" + str(waterRemain) + "吨，相比昨日少了"+ str(DValue) + "吨。"
        alert.sendNotify(NotifyContent, "水表每日汇报", "water")
    time.sleep(5)
    if  elecRemain <= 25:
        alertContent = "当前电表余量" + str(elecRemain) + "kWh，已不足kWh，请及时充值。（点击跳转）"
        alert.sendAlert(alertContent , "电表余量不足25kWh" , "elec")
    else:
        DValue = latestElec - elecRemain
        NotifyContent = "当前电表剩余" + str(elecRemain) + "kWh，相比昨日少了"+ str(DValue) + "kWh。"
        alert.sendNotify(NotifyContent, "电表每日汇报", "elec")
    dataProcess.addData(waterRemain, elecRemain)
    pass

print(timestamp, " ", "First run start.")
main()
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(timestamp, " ", "First run complete.")

# create a scheduler object
scheduler = sched.scheduler(time.time, time.sleep)

 # calculate the number of seconds until 10am
now = time.time()
next_run = now - (now % 86400) + (10 * 3600)
if next_run < now:
    next_run += 86400

# schedule the first run for 10am
scheduler.enterabs(next_run, 1, main)
    
while True:
    # start the scheduler
    print(timestamp, " ", "Waiting for next run")
    scheduler.run()
    
