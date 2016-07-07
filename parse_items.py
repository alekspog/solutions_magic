from selenium import webdriver
import re

driver = webdriver.Firefox()
driver.implicitly_wait(10)
link = "https://market.yandex.ru/catalog/54726/list?hid=91491&how=dpop&in-stock=1&page=2"
driver.get(link)

item_names = driver.find_elements_by_css_selector('.snippet-card__header-text')
item_hrefs = driver.find_elements_by_css_selector('.snippet-card__header-link')

for item in item_names:
    print(item.text)

for item in item_hrefs:
    # print(item.get_attribute('href'))
    result = re.search("https://market.yandex.ru/product/(\d*)", item.get_attribute('href'))
    if result:
        print result.groups()[0]

driver.close()


