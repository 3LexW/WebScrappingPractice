# Install packages
import requests
import time
import string
from bs4 import BeautifulSoup
from selenium import webdriver

# Request website's source code
url = 'https://racing.hkjc.com/racing/information/english/Racing/LocalResults.aspx?RaceDate=2020/07/15&Racecourse=HV&RaceNo=1'
date = url[url.find("RaceDate=") + 9: url.find("RaceDate=") + 19]
course = url[url.find("Racecourse=") + 11: url.find("Racecourse=") + 13] 
raceNo = url[url.find("RaceNo=") + 7:]

browser = webdriver.Chrome('./chromedriver')
browser.get(url)
time.sleep(3)
# print(browser.page_source)

print('Race Date: ', date, ', Race Course: ', course, ', Race Number: ', raceNo, "\n")
# =============== Start web scraping ===============
soup = BeautifulSoup(browser.page_source, 'html.parser')
performance = soup.find("div", {"class": "performance"})
table = performance.find("table")
tbody = table.find("tbody")

#=============== Reach the table body, begin retrieve information ===============
for tr in tbody.find_all("tr"):
    # Generate a loop to create the information needed
    row = []
    for td in tr.find_all("td"):
        a = td.find("a")
        poss = td.find_all("div", {
                           "style": "text-align:center; vertical-align: text-top; width:16px; height:16px; display:inline-block; font-size: 12px;"})

        if a is not None:
            row.append(str(a.string).strip("\n").strip() + str(td.text).strip("\n").strip())
        elif len(poss) != 0:
            poslist = []
            for pos in poss:
                poslist.append(str(pos.string).strip("\n").strip())
            row.append(poslist)
        else:
            row.append(str(td.string).strip("\n").strip())
    print(row)
