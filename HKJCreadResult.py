# Install packages
import requests
import time
import string
import csv
from bs4 import BeautifulSoup
from selenium import webdriver

# =============== Create CSV file ===============
with open('HKJCResults.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    # =============== Header of the file ===============
    writer.writerow(["Date", "Race Number", "Place", "Horse No.", "Horse", "Jockey", "Trainer",
                     "Actual Wt.", "Declare. Horse Wt.", "Draw", "LBW", "Running Position", "Finish Time", "Win Odds"])

    baseUrl = 'https://racing.hkjc.com/racing/information/english/Racing/LocalResults.aspx'

    # =============== Obtain the list of dates for search ===============
    # open website
    browser = webdriver.Chrome('./chromedriver')
    browser.get(baseUrl)
    time.sleep(3)
    soup = BeautifulSoup(browser.page_source, 'html.parser')
    dates = soup.find_all("option")

    # Create date list
    datelist = []
    for date in dates:
        datelist.append(str(date.string))

    # =============== Obtain the information available===============
    for date in datelist:
        raceNo = 1
        url = baseUrl + '?RaceDate=' + date + "&RaceNo=" + str(raceNo)
        browser.get(url)
        soup = BeautifulSoup(browser.page_source, 'html.parser')

        while soup.find("div", {"class": "performance"}) is not None:
            table = soup.find("div", {"class": "performance"}).find(
                "table").find("tbody")
            for tableRow in table.find_all("tr"):
                row = []
                row.append(date)
                row.append(raceNo)
                for tableField in tableRow.find_all("td"):
                    a = tableField.find("a")
                    poss = tableField.find_all("div", {
                        "style": "text-align:center; vertical-align: text-top; width:16px; height:16px; display:inline-block; font-size: 12px;"})

                    if a is not None:
                        row.append(str(a.string).strip("\n").strip() +
                                   str(tableField.text).strip("\n").strip())
                    elif len(poss) != 0:
                        poslist = []
                        for pos in poss:
                            poslist.append(
                                str(pos.string).strip("\n").strip())
                        row.append(poslist)
                    else:
                        row.append(str(tableField.string).strip("\n").strip())
                writer.writerow(row)

            # GO for next page
            raceNo += 1
            url = baseUrl + '?RaceDate=' + date + "&RaceNo=" + str(raceNo)
            browser.get(url)
            soup = BeautifulSoup(browser.page_source, 'html.parser')

    browser.close()