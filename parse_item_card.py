from selenium import webdriver
import numpy as np

driver = webdriver.Firefox()
driver.implicitly_wait(10)
id_list = [10495456, 13485518, 13527763, 13332007, 13485515, 13584121, 12858630, 13584123, 11031621, 12859246, 13471372, 13747914, 13340756, 12259780, 13630660, 12854962, 13340782]
for id in id_list:
    link = "https://market.yandex.ru/product/" + str(id) + "/spec?hid=91491&track=char"
    driver.get(link)

    # criteria_list_el = np.array(driver.find_elements_by_css_selector("dt.product-spec__name > span"))
    criteria_list_el = driver.find_elements_by_id("product-spec-")
    # criteria_list = []
    for criteria in criteria_list_el:
        criteria_name = criteria.find_element_by_css_selector(".product-spec__name-inner")
        value = criteria.find_element_by_css_selector(".product-spec__value-inner")
        print str(id) + "$$$ $$$ $$$" + criteria_name.text + "$$$" + value.text

driver.close()
