from selenium import webdriver
from selenium.webdriver.chrome.service import Service

serviceObject = Service("C:\Driver\chromedriver107.exe")
#make sure you have downloaded the existing chrome version in your pc
driver = webdriver.Chrome(service=serviceObject)

driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.back()
driver.get("https://rahulshettyacademy.com/seleniumPractise/#/")
driver.forward()
