from selenium import webdriver
import os
import time


class CovidBot:

    def __init__(self, id, fullname):
        self.id = id
        self.fullname = fullname

        self.driver = webdriver.Chrome('./chromedriver')
        self.driver.get('<<put form website>>')
        
        self.runCovidBot()

    def runCovidBot(self):
        
        time.sleep(2)
        self.driver.find_element_by_name('data[page3SiAutorizo]').click()

        time.sleep(2)
        self.driver.find_element_by_name('data[identificacion_usuario]').send_keys(self.id)
        self.driver.find_element_by_name('data[nombre_usuario]').send_keys(self.fullname)

        time.sleep(2)
        self.driver.find_element_by_name('data[page1Siguiente]').click()

        time.sleep(2)
        self.driver.find_element_by_name('data[page2Finalizar]').click()

        time.sleep(5)
        self.driver.quit()

if __name__ == '__main__':
    covid_bot = CovidBot('<<My ID number>>', '<<My name>>')
