from django.shortcuts import render
from cmdb import models
# Create your views here.

from urllib.request import Request, urlopen
from bs4 import BeautifulSoup

slist = ['https://xueqiu.com/S/AMZN', 'https://xueqiu.com/S/NVDA','https://xueqiu.com/S/GOOGL','https://xueqiu.com/S/BABA','https://xueqiu.com/S/00700']


def getHTMLText(urls):
    res = []
    try:
        for url in urls:
            r = urlopen(Request(url, headers={'User-Agent': 'Mozilla/5.0'}))
            res.append(r.read())
        return res
    except:
        print(1)
        return []


def getStockList(htmls):
    res = []
    for html in htmls:
        soup = BeautifulSoup(html, 'html.parser')
        temp = soup.find_all(True, attrs={'class': ['stock-name', 'stock-current', 'stock-time', 'stock-change']})

        stockName = temp[0].text.split('(')[0]
        stockPrice = temp[1].text.split('.')[0]
        stockChange = temp[2].text.split('（')[1][:-1]
        stockTime = temp[3].text.split(':')[0]

        res.append((stockName, stockPrice, stockChange, stockTime))
    return res


def index(request):
    if request.method == "POST":
        models.UserInfo.objects.all().delete()
        stockInfos = getStockList(getHTMLText(slist))
        for info in stockInfos:
            models.UserInfo.objects.create(name=info[0], price=info[1], change=info[2], time=info[3])
    stock_list = models.UserInfo.objects.all()
    return render(request, "index.html", {"data": stock_list})
