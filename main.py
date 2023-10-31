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
    print("Waiting for next run")
    scheduler.run()
