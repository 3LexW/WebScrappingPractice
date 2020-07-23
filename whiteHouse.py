#Goal: Extract all of the links on the page that point to the briefings and statements

#Install packages
import requests
from bs4 import BeautifulSoup

#Request website
result = requests.get("https://www.whitehouse.gov/briefings-statements/")
print(result.status_code, "\n")

#Create BeautifulSoup content
soup = BeautifulSoup(result.content, 'html.parser') 

#In this website, all the statements are inside the h2 class - Example
#<h2 class="briefing-statement__title"><a href="https://www.whitehouse.gov/briefings-statements/bill-announcement-072220/">Bill Announcement</a></h2>

#Goal h2 -> a -> url
urls = []

for h2_tag in soup.find_all("h2"):
    a_tag = h2_tag.find("a")
    urls.append(a_tag.attrs["href"])

print(urls)