import json
from linebot import LineBotApi
from linebot.models import TextSendMessage
import requests
from bs4 import BeautifulSoup

file=open('info.json', 'r')
info=json.load(file)

CHANNEL_ACCESS_TOKEN = info['CHANNEL_ACCESS_TOKEN']
LineBotApi = LineBotApi(CHANNEL_ACCESS_TOKEN)

def main():
    url2 = "https://weather.yahoo.co.jp/weather/jp/14/4620.html"
    res = requests.get(url2)
    soup = BeautifulSoup(res.content, 'html.parser')

    #以下で各情報を取得
    hiduke = soup.find(class_="date").text
    hiduke = hiduke.strip()
    telop = soup.find("p", class_="pict").text
    telop = telop.strip()
    highlists = soup.find("li",class_="high").text
    lowlists = soup.find("li",class_="low").text
    kousui = soup.find_all(class_="precip")[0]
    kousui612 = kousui.find_all("td")[1].text
    kousui1218 = kousui.find_all("td")[2].text
    kousui1824 = kousui.find_all("td")[3].text

    hiduke_t = soup.find_all(class_="date")
    hiduke_t = hiduke_t[1].text
    hiduke_t = hiduke_t.strip()
    telop_t = soup.find_all("p", class_="pict")
    telop_t = telop_t[1].text
    telop_t=telop_t.strip()
    highlists_t = soup.find_all("li",class_="high")
    highlists_t = highlists_t[1].text
    lowlists_t = soup.find_all("li",class_="low")
    lowlists_t = lowlists_t[1].text
    kousui = soup.find_all(class_="precip")[0]
    kousui612 = kousui.find_all("td")[1].text
    kousui1218 = kousui.find_all("td")[2].text
    kousui1824 = kousui.find_all("td")[3].text
    kousui_t = soup.find_all(class_="precip")[1]
    kousui006_t = kousui_t.find_all("td")[0].text
    kousui612_t = kousui_t.find_all("td")[1].text
    kousui1218_t = kousui_t.find_all("td")[2].text
    kousui1824_t = kousui_t.find_all("td")[3].text

    messeges_ = "Good Mooning!!!\n" + hiduke + "の小田原の天気" + "\n" + telop + "\n" + "最高気温：" + highlists + "\n" +\
                "最低気温：" + lowlists + "\n" + "降水確率 6-12時 ：" + kousui612 + "\n" +"　　　　 12-18時：" + kousui1218+"\n"+\
                "　　　　 18-24時："+kousui1824+"\n"+"\n"+hiduke_t+"の小田原の天気"+"\n"+telop_t + "\n" + "最高気温：" + highlists_t + "\n" +\
                "最低気温：" + lowlists_t + "\n" + "降水確率 0-6時  ："+kousui006_t+"\n"+"　　　　 6-12時 ：" + kousui612_t + "\n" +"　　　　 12-18時：" + kousui1218_t+"\n"+\
                "　　　　 18-24時："+kousui1824_t

    USER_ID=info['USER_ID']
    messages=TextSendMessage(text=messeges_)
    LineBotApi.push_message(USER_ID, messages=messages)

if __name__ == "__main__":
    main()