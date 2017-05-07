import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
tags = raw_input('Enter the tags for getting top posts links :  ')
driver = webdriver.Firefox()
driver.implicitly_wait(30)
driver.get("http://stackoverflow.com/questions")
time.sleep(1)
if tags:
    driver.find_element_by_name("q").clear()
    driver.find_element_by_name("q").send_keys(tags)
    time.sleep(1)
    driver.find_element_by_css_selector("button.btn.js-search-submit").click()
    time.sleep(1)
try:
    driver.find_element_by_css_selector('a[title="tag wiki"]')
    flag = True
except Exception, e:
    flag = False
driver.find_element_by_link_text("votes").click()
time.sleep(1)
no_of_questions_per_page = driver.find_element_by_xpath(
    '//div[@class="page-sizer fr"]/a[@class="page-numbers current"]').text
required_number_of_posts = 30
number_of_pages = required_number_of_posts / int(no_of_questions_per_page)

print "#########################################Top Questions##################################"
if number_of_pages >= 1:
    for i in range(number_of_pages):
        for j in range(int(no_of_questions_per_page)):

            if flag:
                xpath = "//div[@id='questions']/div[" + \
                    str(j + 1) + "]/div[2]/h3/a"
                print driver.find_element_by_xpath(xpath).get_attribute('href')
            else:
                xpath = "//div[@class='search-results js-search-results']/div[" + \
                    str(j + 1) + "]/div[2]/div[1]/span/a"
                print driver.find_element_by_xpath(xpath).get_attribute('href')

    try:
        driver.find_element_by_xpath(
            '//div[@class="pager fl"]/a[6]/span[@class="page-numbers next"]').click()
        driver.implicitly_wait(60)
    except:
        print "All questons loaded"
