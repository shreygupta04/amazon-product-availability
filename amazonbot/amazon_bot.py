from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

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
    options.add_argument("--headless")
    driver = webdriver.Chrome(executable_path="/Users/shreygupta/Documents/ComputerScience/PythonLanguage/AmazonAvailabilityBot/amazonbot/chromedriver", options=options)

    def __init__(self):
        self.products = {}

    def search(self, keywords):
        search = keywords.replace(' ', '+')
        keywords = keywords.split()
        self.driver.get('https://www.amazon.com/s?k={}&ref=nb_sb_noss_2'.format(search))
        i = 1
        containers = self.driver.find_elements_by_xpath(
            "//div[@class='s-expand-height s-include-content-margin s-border-bottom s-latency-cf-section']")
        for container in containers:
            create = True
            title = container.find_element_by_xpath(".//span[@class='a-size-base-plus a-color-base a-text-normal']").text
            try:
                availability = container.find_element_by_xpath(".//div[@class='a-row a-size-base a-color-secondary']").text
            except NoSuchElementException:
                availability = '-1'
            link = container.find_element_by_xpath(".//a[@class='a-link-normal a-text-normal']").get_attribute('href')
            for word in keywords:
                if word.lower() not in title.lower():
                    create = False
            if availability.startswith('Currently unavailable') or availability.startswith('In stock on') or availability.startswith('by') or availability.startswith('Out of'):
                create = False
            if create:
                self.products['product' + str(i)] = {
                    'title': title,
                    'availability': availability,
                    'link': link
                }
                i += 1
        return self.products


