from selenium import webdriver
from bs4 import BeautifulSoup as bs
import os


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
            availability = container.select_one("div.a-row.a-size-base.a-color-secondary > span")
            if availability:
                availability = availability.get('aria-label')
                if availability is None:
                    availability = "-1"
                else:
                    pass
            else:
                availability = "-1"
            link = 'https://www.amazon.com/' + container.select_one("a.a-link-normal.a-text-normal")['href']
            picture = container.select_one("img.s-image")['src']
            for word in keywords:
                if word.lower() not in title.lower():
                    create = False
            if availability.startswith('Currently') or availability.startswith('by') or availability.startswith('Out of') or availability.startswith('Temporarily'):
                create = False
            if create:
                self.products['product' + str(i)] = {
                    'title': title,
                    'availability': availability,
                    'link': link,
                    'picture': picture
                }
                i += 1
        return self.products

