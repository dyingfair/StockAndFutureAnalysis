# _*_coding:utf-8_*_
from urllib.request import urlopen
from bs4 import BeautifulSoup
import requests
import datetime,time,os
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

#https://androidinvest.com/Stock/HistoryPB/SH601668/
head = {
    "User-Agent":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_5)AppleWebKit 537.36 (KHTML, like Gecko) Chrome",
    "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8"
    }

def get_history_date_mean(data):
    len_data = len(data)
    history_mean = []
    for i in range(len(data)) :
        history_mean.append(np.mean(data[0:i+1]))
    return history_mean

def get_stock_code(stock_code):
    str_stock_code= str(stock_code)
    if len(str_stock_code) != 6:
        print("the length of stock code is not correct")
        return ""
    if str_stock_code[0] not in '6023' or not str_stock_code.isdigit():
        print("stock code is not correct")
        return ""
    elif(str_stock_code[0] == '6'):
        return 'SH' + str_stock_code
    else:
        return 'SZ' + str_stock_code

def get_stock_koufei_PE(str_stock_code):
    url = "https://androidinvest.com/Stock/History/" + str_stock_code + "/"
    session = requests.Session()
    req = session.get(url, headers=head)
    stock_info = req.text
    bsObj = BeautifulSoup(req.text, "html.parser")
    PE_data = bsObj.find_all('div', id='chart_koufei')[0].get_text()
    date, PE, stock_price, _, _ = PE_data.split('@')
    date = eval(date)
    PE = eval(PE)
    stock_price = eval(stock_price)

    stock_name = bsObj.find_all('meta')[2].attrs['content']
    stock_name = stock_name[0: stock_name.find('(')]
    plt.plot(date,PE,label="PE" )
    plt.plot(date, get_history_date_mean(PE), label = 'mean PE')
    plt.ylabel(str_stock_code + "  PE")
    plt.xlabel("date")
    plt.xticks(date[:: (int(len(date) / 10) + 1)])
    plt.title(stock_name + "历史扣非市盈率")
    plt.legend()
    plt.show()

def get_stock_history_PB(str_stock_code):
    url = "https://androidinvest.com/Stock/HistoryPB/" + str_stock_code + "/"
    session = requests.Session()
    req = session.get(url, headers=head)
    stock_info = req.text
    bsObj = BeautifulSoup(req.text, "html.parser")
    PE_data = bsObj.find_all('div', id='chart4')[0].get_text()
    date, PB, stock_price, _, _ = PE_data.split('@')
    date = eval(date)
    PB = eval(PB)
    stock_price = eval(stock_price)

    stock_name = bsObj.find_all('meta')[2].attrs['content']
    stock_name = stock_name[0: stock_name.find('(')]
    plt.plot(date,PB,label="PB" )
    plt.plot(date, get_history_date_mean(PB), label = 'mean PB')
    plt.ylabel(str_stock_code + "  PB")
    plt.xlabel("date")
    plt.xticks(date[:: (int(len(date) / 10) + 1)])
    plt.title(stock_name + "历史市净率")
    plt.legend()
    plt.show()


def get_stock_PE_PB(str_stock_code):
    url = "https://androidinvest.com/Stock/History/" + str_stock_code + "/"
    session = requests.Session()
    req = session.get(url, headers=head)
    stock_info = req.text
    bsObj = BeautifulSoup(req.text, "html.parser")
    PE_data = bsObj.find_all('div', id='chart_koufei')[0].get_text()
    date, PE, stock_price, _, _ = PE_data.split('@')
    date = eval(date)
    PE = eval(PE)
    stock_price = eval(stock_price)

    stock_name = bsObj.find_all('meta')[2].attrs['content']
    stock_name = stock_name[0: stock_name.find('(')]

    url = "https://androidinvest.com/Stock/HistoryPB/" + str_stock_code + "/"
    session = requests.Session()
    req = session.get(url, headers=head)
    stock_info = req.text
    bsObj = BeautifulSoup(req.text, "html.parser")
    PE_data = bsObj.find_all('div', id='chart4')[0].get_text()
    _, PB, _, _, _ = PE_data.split('@')
    PB = eval(PB)

    fig = plt.figure()
    ax1 = fig.add_subplot(211)
    ax1.plot(date,PE,'r',label="PE" )
    ax1.plot(date, get_history_date_mean(PE),'g', label = 'mean PE')
    ax1.set_ylabel(str_stock_code + "  PE")
    ax1.set_xlabel("date")
    ax1.set_xticks(date[:: (int(len(date) / 10) + 1)])
    ax1.set_title (stock_name + "历史扣非市盈率")
    ax1.yaxis.grid(True)
    plt.legend(loc = 2)
    ax2 = ax1.twinx()  # this is the important function
    ax2.plot(date, stock_price, 'b',label="price")
    ax2.set_ylabel('Price')
    ax2.set_xticks(date[:: (int(len(date) / 10) + 1)])
    plt.legend(loc = 1)

    ax3 = fig.add_subplot(212)
    ax3.plot(date,PB,'r',label="PB" )
    ax3.plot(date, get_history_date_mean(PB), 'g',label = 'mean PB')
    ax3.set_ylabel(str_stock_code + "  PB")
    ax3.set_xlabel("date")
    ax3.set_xticks(date[:: (int(len(date) / 10) + 1)])
    ax3.set_title(stock_name + "历史市净率")
    ax3.yaxis.grid(True)
    plt.legend(loc = 2)
    ax4 = ax3.twinx()  # this is the important function
    ax4.plot(date, stock_price, 'b', label="price")
    ax4.set_ylabel('Price')
    ax4.set_xticks(date[:: (int(len(date) / 10) + 1)])
    plt.legend(loc = 1)

    plt.show()


stock_code = input("Please input the stock code(6 numbers): ")
str_stock_code = get_stock_code(stock_code)

if 0 !=  len(str_stock_code):
    get_stock_PE_PB(str_stock_code)
