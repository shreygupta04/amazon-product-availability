from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from bs4 import BeautifulSoup as bs
import os

# search = input().replace(' ', '+')

# headers = {
#     'authority': 'www.amazon.com',
#     'pragma': 'no-cache',
#     'cache-control': 'no-cache',
#     'dnt': '1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36',
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
#     'sec-fetch-site': 'none',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-dest': 'document',
#     'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
# }
# response = requests.get('https://www.amazon.com/s?k={}&ref=nb_sb_noss_2'.format(search), headers=headers, verify=False)
# soup_file = bs(response.text, 'html.parser')
#
# containers = soup_file.findAll("div", {"class": "sg-col-inner"})
# print(containers)


class AmazonProductAvailability:
    options = webdriver.ChromeOptions()
    if os.environ.get('GOOGLE_CHROME_BIN'):
        options.binary_location = os.environ['GOOGLE_CHROME_BIN']

    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')

    driver = webdriver.Chrome(executable_path=os.environ.get('CHROMEDRIVER_PATH'), options=options)

    def __init__(self):
        self.products = {}

    def search(self, keywords):
        search = keywords.replace(' ', '+')
        keywords = keywords.split()
        self.driver.get('https://www.amazon.com/s?k={}&ref=nb_sb_noss_2'.format(search))
        self.driver.implicitly_wait(1)
        soup_file = bs(self.driver.page_source, 'html.parser')
        i = 1
        containers = soup_file.select("div.s-expand-height.s-include-content-margin.s-border-bottom.s-latency-cf-section")
        for container in containers:
            create = True
            title = container.select_one("span.a-size-base-plus.a-color-base.a-text-normal").text
            availability = container.select_one("div.a-row.a-size-base.a-color-secondary")
            if availability:
                availability = availability.text
            else:
                availability = "-1"
            link = 'https://www.amazon.com/' + container.select_one("a.a-link-normal.a-text-normal")['href']
            picture = container.select_one("img.s-image")['src']
            for word in keywords:
                if word.lower() not in title.lower():
                    create = False
            if availability.startswith('Currently unavailable') or availability.startswith('In stock on') or availability.startswith('by') or availability.startswith('Out of'):
                create = False
            if create:
                self.products['product' + str(i)] = {
                    'title': title,
                    'availability': availability,
                    'link': link,
                    'picture': picture
                }
                i += 1
        print(self.products)
        return self.products

