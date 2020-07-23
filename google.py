#Install the packages
import requests                     #Access webpage
from bs4 import BeautifulSoup       #Web scraping tool

#Using request package, use get function to obtain the website
result = requests.get("https://www.google.com")

#Check the website is accessible, OK response should be 200
#For other code, check https://zh.wikipedia.org/zh-hk/HTTP%E7%8A%B6%E6%80%81%E7%A0%81
#print(result.status_code)

#Print some extra information
#for key in result.headers:
#    print(key, ":", result.headers[key])

#Retrieve the content of the webpage
src = result.content

#Begin parse and process the source using a beautifulSoup object
soup = BeautifulSoup(src, 'html.parser')

#Using the soup object, we can now retrieve some specific information
#One example could be the links inside in webpage, using the <a> tags
links = soup.find_all("a")
#print(links)
#print("\n")

for link in links:
    if "關於" in link.text:
        print(link)
        print(link.attrs['href'])   #Attributes, such as class, href

