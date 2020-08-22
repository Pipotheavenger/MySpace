# -*- coding: utf-8 -*-
"""
Created on Thu Aug 20 11:48:09 2020

@author: Felipe Valencia
"""


import time
import requests
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
import pyautogui


#chrome_options= Options()
#chrome_options.add_argument("--headless")
#chrome_options=chrome_options,
#Son las coordenadas para que el mouse haga click()
time.sleep(6)
a=pyautogui.position()
print(a)
position=[777,467,1092,465,287,166,764,515,372,164,769,612,678,452,168,607,1336,693,1140,239,1029,628,570,695]
#Crea el navegador y se registra por usted señor

ns='https://sicuaplus.uniandes.edu.co/'
driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
driver.get(ns)
driver.maximize_window()
driver.find_element_by_xpath('/html/body/div/div/div[2]/a[1]/p').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="i0116"]').send_keys("sf.valencia@uniandes.edu.co")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="idSIButton9"]').click()
time.sleep(5)
driver.find_element_by_xpath('//*[@id="passwordInput"]').send_keys("sebastian13")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="submitButton"]').click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="agree_button"]').click()
time.sleep(2)
######
driver.find_element_by_xpath('//*[@id="_25_1termCourses_noterm"]/ul/li[1]/a').click()
#driver.find_element_by_xpath('//*[@id="_25_1termCourses_noterm"]/ul/li[14]/a').click()
time.sleep(6)    
pyautogui.click(position[0],position[1])
time.sleep(6)
pyautogui.click(position[2],position[3])
time.sleep(30)
pyautogui.click(position[4],position[5])
time.sleep(4)
pyautogui.click(position[6],position[7])
time.sleep(4)
pyautogui.click(position[8],position[9])
time.sleep(4)
pyautogui.click(position[10],position[11])
time.sleep(7)
pyautogui.click(position[12],position[13])
time.sleep(6)
pyautogui.click(position[14],position[15])
time.sleep(2)
pyautogui.click(position[16],position[17])
time.sleep(2)
pyautogui.click(position[18],position[19])
time.sleep(2)
pyautogui.click(position[20],position[21])
time.sleep(2)
pyautogui.typewrite("Recursos Python")
pyautogui.typewrite("\n")
time.sleep(2)
pyautogui.click(position[22],position[23])
pyautogui.move(position[16],position[17])

