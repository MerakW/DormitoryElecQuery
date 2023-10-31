from requests import get
from json import load
from os import path

#获取当前文件路径，转换为相对路径，并为配置文件路径赋值
dirPath = path.dirname(path.abspath(__file__))
filePath = path.join(dirPath, "Config.json")

#读取配置文件
with open(filePath,'r') as fr: 
	Configs = load(fr)
 
barkKey = Configs["barkKey"]
 
def sendNotify(text, title, Form):
    if  Form == "water":
        iconUrl = "https://z1.ax1x.com/2023/10/31/ping3WR.png"
    elif  Form == "elec":
        iconUrl = "https://z1.ax1x.com/2023/10/31/pingGS1.png"
    url = "https://api.day.app/" + barkKey + "/" + title + "/" + text+"/?icon="+iconUrl+"&group="+Form
    get(url)

def sendAlert(text, title, Form):
    if  Form == "water":
            iconUrl = "https://z1.ax1x.com/2023/10/31/pingWTg.png"
    elif  Form == "elec":
            iconUrl = "https://z1.ax1x.com/2023/10/31/pinghkQ.png"
    url = "https://api.day.app/" + barkKey + "/" + title + "/" + text+"/?level=timeSensitive&url=shortcuts://run-shortcut?name=StartDormitoryElecCharge"+"&icon="+iconUrl+"&group="+Form
    get(url)
    