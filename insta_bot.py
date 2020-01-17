from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

class Instagram:

    def __init__(self):
        self.driver = webdriver.Chrome('') #Passar path do driver
        self.driver.get('https://www.instagram.com/accounts/login/?hl=pt-br&source=auth_switcher')
        time.sleep(1)
        self.action = ActionChains(self.driver)

    def login(self, user_name, password):
        self.username = user_name
        self.password = password
        
        #Username informations
        user_name_info = self.driver.find_element_by_xpath('//input[@name="username"]')
        user_name_info.clear()
        user_name_info.send_keys(self.username)
        time.sleep(1)

        #Password informations
        user_password_info = self.driver.find_element_by_xpath('//input[@name="password"]')
        user_password_info.clear()
        user_password_info.send_keys(self.password)
        time.sleep(1)

        #Submit credentials
        submit_button = self.driver.find_element_by_xpath('//button[@type="submit"]')
        submit_button.click()
        time.sleep(5)

        #declaim
        
        """
        document.body.scrollHeight
        """
        
    def scroll(self):
        for _ in range(40):
            time.sleep(2)
            self.driver.execute_script("window.scrollTo(0,  document.body.scrollHeight);")
            
    def likes(self, hashtag):
        driver = self.driver
        driver.get('https://www.instagram.com/explore/tags/' + hashtag + '/')
        time.sleep(2)

        for _ in range(1, 3):# this is for each line of photo
            driver.execute_script("window.scrollTo(0,  document.body.scrollHeight);")
            time.sleep(2)
        href = driver.find_elements_by_tag_name('a')
        pic = [elem.get_attribute('href') for elem in href]
        [href for href in pic if hashtag in href]
        print('pics ' + str(len(pic)))

        for x in pic:
            time.sleep(2)
            driver.get(x)
        
    def feed(self, y): #Likes no feed
        self.y = y

        for _ in range(1000):
            
            #self.driver.execute_script("window.scrollTo(0., "+str(self.y)+");")
            self.driver.execute_script("window.scrollTo(0,document.body.scrollHeight)")
            time.sleep(5)
            #try:
            self.driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]').click()
            #except selenium.common.exceptions.ElementClickInterceptedException:
                #continue
            '''
                self.button = self.driver.find_element_by_xpath('//button[@class="dCJp8 afkep"]')
                self.button.click()
                time.sleep(2)
            '''        