from selenium import webdriver
import cv2
import time
from dataScraper import faceshot

class webDrive:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Python36\\selenium\\webdriver\\chrome\\chromedriver.exe")
        search = "searchTerms.txt"
        with open(search) as f:
            self.terms = f.read().splitlines()

        self.face = faceshot.faceFinder()

    def browse(self):
        driver = self.driver
        driver.get('https://www.youtube.com')

        for term in self.terms:
            search = driver.find_element_by_id('search')
            search.click()
            search.send_keys(term)
            search = driver.find_element_by_id('search-icon-legacy')
            search.click()
            time.sleep(2)
            # results = driver.find_elements_by_id('video-title')
            results = driver.find_elements_by_class_name('title-and-badge')#('ytd-video-renderer')
            for result in results:
                print(len(results))
                result.click()
                time.sleep(3)
                cname = driver.find_element_by_xpath(
                    '/html/body/ytd-app/div/ytd-page-manager/ytd-watch-flexy/div[3]/div[1]/div/div[7]/div[3]/ytd-video-secondary-info-renderer/div/div[2]/ytd-video-owner-renderer/div[1]/div/yt-formatted-string/a')
                chName = (cname.get_attribute('text'))
                self.face.isFaceScreen(chName,30,2)

                time.sleep(4)
                driver.back()
            time.sleep(5)
            driver.back()

        driver.close()

if __name__=='__main__':
    n = webDrive()
    n.browse()
