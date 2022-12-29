from audioop import add
from lib2to3.pgen2 import driver
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://abhinav7076.github.io/csb-0p7oz7/")  

time.sleep(3) 

sign_up = driver.find_element("xpath", "//input[@placeholder='Enter name']")
sign_up.send_keys('hello')
time.sleep(1)
add_btn = driver.find_element("xpath", "//button[normalize-space()='Add new experience']")
add_btn.click()
driver.close()