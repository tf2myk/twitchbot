# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

class clipbot():

  def __init__(self, vids, link):
    self.vids = vids
    self.link = link

  def setup_method(self):
    options = webdriver.ChromeOptions()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    self.vars = {}
  
  def teardown_method(self):
    self.driver.quit()
  
  def clipdownload(self):
    self.driver.get(self.link)
    self.driver.maximize_window()

    for i in range(1, self.vids+1):
      name = ".h-full:nth-child(" + str(i) + ")> .flex-col"
      #print(name)
      self.driver.find_element(By.CSS_SELECTOR, name).click()
      WebDriverWait(self.driver, 20).until(expected_conditions.element_to_be_clickable((By.XPATH, "/html/body/main/div[2]/div/div[3]/div/div[2]/div[1]/div/a")))
      self.driver.find_element(By.XPATH, "/html/body/main/div[2]/div/div[3]/div/div[2]/div[1]/div/a").click()
      #time.sleep(0.2)
      if i >= self.vids:
        print("Done")
        self.driver.execute_script('''window.open("https://media1.giphy.com/media/26u4lOMA8JKSnL9Uk/giphy.gif?cid=790b7611a4d0b9525938666946ee75ebb87f7f6b5e715a39&rid=giphy.gif&ct=g","_blank");''')
        #self.teardown_method()
      else:
        self.driver.get(self.link)

vidsnum = input("How many vids: ")
cliplink = input("Enter streamscharts clip link example: https://streamscharts.com/clips?game=league-of-legends\n")

while "https://streamscharts.com/clips?game=" not in cliplink:
  cliplink = input("Incorrect link used, example: https://streamscharts.com/clips?game=league-of-legends\n")

clipper = clipbot(int(vidsnum),cliplink)
clipper.setup_method()
clipper.clipdownload()
