# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 00:06:08 2020

@author: Felipe Valencia
"""


import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime
import time
import random
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options


l = input("Escriba la banda deseada ")
banda = l.split(" ")

URL= 'https://www.last.fm/search/tracks?q='+"+".join(banda)
headers = {"user-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}


def obtener_Titulos():
    page = requests.get(URL,headers=headers)      
    soup = BeautifulSoup(page.content , 'html.parser')
    canciones=soup.find_all(class_="chartlist-name")
    great=[]
    for i in canciones:
        great.append(i.text)
        print(i.text)
    return great

def aleat(lista):
    num = random.randint(0,len(lista)-1)
    indicada=lista[num].split(' ')
    print(indicada)
    driver = webdriver.Chrome(executable_path=r"C:\webdrivers\chromedriver.exe")
    driver.get('https://www.youtube.com/results?search_query='+"+".join(l)+"+".join(indicada))
    iniciar=driver.find_element_by_xpath('//*[@id="dismissable"]').click()


aleat(obtener_Titulos())  
    
#Falta adecuarlo a alexa ( hacer que salte los anuncios y pregunte cosas )y hacer un nuevo escript que recopile todos los links de internet y los descargue   