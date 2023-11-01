import schedule
import time
from json import load
from os import path
import datetime
import threading
import keyboard
import query

timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#获取当前文件路径，转换为相对路径，并为配置文件路径赋值
dirPath = path.dirname(path.abspath(__file__))
filePath = path.join(dirPath, "Config.json")

#读取配置文件
with open(filePath,'r') as fr: 
	Configs = load(fr)

Today = datetime.date.today()
Tomorrow = Today + datetime.timedelta(days=1)

print(timestamp, " ", "First report start.")
query.Report()
timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
print(timestamp, " ", "First report complete.")

print(timestamp, " ", "Waiting for next report at ", Tomorrow, "10:30.")

def Daily():
    query.dailyReport()

def Hourly():
    query.queryHourly()

# 每天的10:30执行Main函数
schedule.every().day.at("10:30").do(Daily)

# 每2小时执行Hourly函数
schedule.every().day.at("00:00").do(Hourly)
schedule.every().day.at("02:00").do(Hourly)
schedule.every().day.at("04:00").do(Hourly)
schedule.every().day.at("06:00").do(Hourly)
schedule.every().day.at("08:00").do(Hourly)
schedule.every().day.at("10:00").do(Hourly)
schedule.every().day.at("12:00").do(Hourly)
schedule.every().day.at("14:00").do(Hourly)
schedule.every().day.at("16:00").do(Hourly)
schedule.every().day.at("18:00").do(Hourly)
schedule.every().day.at("20:00").do(Hourly)
schedule.every().day.at("22:00").do(Hourly)

def main():
    print(timestamp, " ", "Main thread start.")
    while True:
        schedule.run_pending()
        time.sleep(1)

# 创建线程并启动
t = threading.Thread(target=main, daemon=True)
t.start()
# 等待esc键按下
keyboard.wait('esc')
