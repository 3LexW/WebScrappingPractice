# WebScrappingPractice

## Practice 1. Obtain URL from [Google](google.com)
Please find file [google.py](https://github.com/3LexW/WebScrappingPractice/blob/master/google.py) for code

## Practice 2. Extract all of the links from [White House](https://www.whitehouse.gov/briefings-statements/) that point to the briefings and statements
Please find file [whiteHouse.py](https://github.com/3LexW/WebScrappingPractice/blob/master/whiteHouse.py) for code

## Practice 3. Obtain most of the races result from [Hong Kong Jockey Club](https://racing.hkjc.com/racing/information/english/Racing/LocalResults.aspx)
Since the request package could not download any source code from the website, web automation tool "Selenium" is introduced, which is a web browser scripting package, mainly for scraping source code from the website.
After the source code is found, BeautifulSoup is then used to obtain the information needed, which is every race result in every racing day available from the website. The information is then extracted to a csv file for further processing.

Please also download [chromedriver.exe](https://github.com/3LexW/WebScrappingPractice/blob/master/chromedriver.exe) to the same folder where the code is placed, and [install selenium](https://selenium-python.readthedocs.io/installation.html) to make the code work.

The running time of the script is longer than an hour since web browser is introduced, therefore it is suggested to modify the code for a quicker test.

Please find file [HKJCreadResult.py](https://github.com/3LexW/WebScrappingPractice/blob/master/HKJCreadResult.py) for code, and [HKJCResults.csv](https://github.com/3LexW/WebScrappingPractice/blob/master/HKJCResults.csv) for the result.
