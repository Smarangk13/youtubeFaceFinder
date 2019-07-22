from selenium import webdriver
import time
import bs4

driver =  webdriver.Chrome("C:\\Python36\\selenium\\webdriver\\chrome\\chromedriver.exe")
driver.get('https://www.youtube.com/watch?v=zAXIxlVjuA8')
# cname = driver.find_element_by_id('owner-name')
time.sleep(3)
cname = driver.find_element_by_xpath('/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[7]/div[3]/ytd-video-secondary-info-renderer/div/div[2]/ytd-video-owner-renderer/div[1]/div/yt-formatted-string/a')
print(cname.get_attribute('text'))

time.sleep(1)
driver.close()