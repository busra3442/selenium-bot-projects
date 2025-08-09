from userInfo import username, password
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

class Github:
    def __init__(self,username,password):
        self.browser = webdriver.Chrome()
        self.username = username
        self.password = password
        self.followers = []

    def signIn(self):
        self.browser.get("https://github.com/login")
        time.sleep(2)

        self.browser.find_element(By.XPATH,"//*[@id='login_field']").send_keys(self.username)
        self.browser.find_element(By.XPATH,"//*[@id='password']").send_keys(self.password)

        time.sleep(1)

        self.browser.find_element(By.XPATH, "/html/body/div[1]/div[3]/main/div/div[2]/form/div[3]/input").click()


    def getFollowers(self):
        self.browser.get("https://github.com/busra3442?tab=followers")
        time.sleep(2)

        items = self.browser.find_elements(By.CSS_SELECTOR,".d-table.table-fixed") # takipçi sayfasından

        for i in items:
            self.followers.append(i.find_element(By.CSS_SELECTOR,".Link--secondary.pl-1").text) # herhangi bir takipçiden

github = Github(username,password)
github.signIn()
github.getFollowers()
print(github.followers)






