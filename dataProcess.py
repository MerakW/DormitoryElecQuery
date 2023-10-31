import csv
import datetime
from os import path

#获取当前文件路径，转换为相对路径，然后对其与子目录文件合并,并为CSV文件路径赋值
dirPath = path.dirname(path.abspath("main.py"))
filePath = dirPath + "\data"
WfilePath = filePath + "\water.csv"
EfilePath = filePath + "\elec.csv"
    
def addData(water, elec):   #添加数据
    # Get current timestamp
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    # Write water data to CSV
    with open(WfilePath, mode='a', newline='') as water_file:
        water_writer = csv.writer(water_file)
        water_writer.writerow([timestamp, water])
    
    # Write electricity data to CSV
    with open(EfilePath, mode='a', newline='') as elec_file:
        elec_writer = csv.writer(elec_file)
        elec_writer.writerow([timestamp, elec])
