from bs4 import BeautifulSoup
from lxml import html
import numpy as np
from sklearn.linear_model import LinearRegression
import urllib.request
import requests
import plotly.plotly as py
import plotly.graph_objs as go
import plotly.tools as tls
from datetime import datetime
import re
import matplotlib.pyplot as plt

# pip install requests
# pip install BeautifulSoup4
# pip install lxml
# pip install numpy
# pip install sklearn
# pip install matplotlib

class NotValidDateFormat(Exception):
    pass

class Webscraping():

    def __init__(self, link):
        self.link = link

    def getdatafromSource(self):
        page = urllib.request.urlopen(self.link)
        soup = BeautifulSoup(page, 'html.parser')
        price_box = soup.find('span', attrs={'data-reactid': 53})
        pricelist = []
        datelist = []
        datelistfloat = []
        pricecounter = 53
        datecounter = 51

        while (True):
            price_box = soup.find('span', attrs={'data-reactid': pricecounter})
            date_box = soup.find('span', attrs={'data-reactid': datecounter})
            if price_box == None:
                pricecounter = pricecounter + 15
                datecounter = datecounter + 15
                continue
            pricelist.append(float(price_box.string))
            date = datetime.strptime(date_box.string, '%b %d, %Y')
            datelistfloat.append(datetime.fromisoformat(str(date)).timestamp())
            datelist.append(str(date.month) + "-" + str(date.day))
            pricecounter = pricecounter + 15
            datecounter = datecounter + 15
            #get first 20 prices
            if pricecounter > 300:
                break
        return pricelist, datelist, datelistfloat

    def drawplot(self, pricelist, datelist):
        pricelist.reverse()
        datelist.reverse()
        plt.plot(datelist, pricelist)
        plt.show()

    def createCsvFile(self, csvfilename, pricelist, datelist):
        dic = dict(zip(datelist, pricelist))
        with open(csvfilename, 'w') as csv_file:
            columntitlerow = "date,price\n"
            csv_file.write(columntitlerow)
            [csv_file.write(key + "," + str(value) + "\n") for key, value in dic.items()]

    def makeprediction(self, pricelist, datelist, newdate):
        if not self.valid_date(newdate):
            raise NotValidDateFormat
        datelist = np.array(datelist).reshape((len(datelist), 1))
        reg = LinearRegression().fit(datelist, pricelist)
        newdate = datetime.strptime(newdate, '%m/%d/%Y')
        newdatetimestamp = datetime.fromisoformat(str(newdate)).timestamp()
        newdata = [(newdatetimestamp)]
        newdata = np.array(newdata).reshape((len(newdata), 1))
        print(str(newdate) + "predicted price =" + str(reg.predict(newdata)))

    def valid_date(selstrptimef, datestring):
        mat = re.match('(\d{2})[/.-](\d{2})[/.-](\d{4})$', datestring)
        if mat is not None:
            return True
        else:
            return False

web = Webscraping('https://finance.yahoo.com/quote/AAPL/history?p=AAPL')
historyList = web.getdatafromSource();
web.drawplot(historyList[0], historyList[1])
web.createCsvFile("C:/Users/omer/Downloads/stocks.csv", historyList[0], historyList[1])
web.makeprediction(historyList[0], historyList[2], '12/30/2018')
