# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 21:53:01 2020

@author: Felipe Valencia
"""

import os
import requests
from bs4 import BeautifulSoup
import smtplib
import subprocess as sub
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options


l = input("Escriba la banda deseada ")
banda = l.split(" ")

URL= 'https://www.last.fm/search/tracks?q='+"+".join(banda)
headers = {"user-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

chrome_options= Options()
chrome_options.add_argument("--headless")



def obtener_Titulos1():
    page = requests.get(URL,headers=headers)      
    soup = BeautifulSoup(page.content , 'html.parser')
    canciones=soup.find_all(class_="chartlist-name")
    great=[]
    for i in canciones:
        great.append(i.text)
    return great

def obtener_Titulos2():
    k= 'https://musicas3.com/'+"-".join(banda)+'.html'
    page = requests.get(k,headers=headers)      
    soup = BeautifulSoup(page.content , 'html.parser')
    canciones=soup.find(id="playlist")
    tudos=canciones.find_all("a")
    b=[]
    for i in range(0,len(tudos)-1):
        b.append(tudos[i].text)
    return b

def links(lista):
    
    for i in range (0,len(lista)-1):
        
        indicada=lista[i].split(' ')
        print(lista[i])
        driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"C:\webdrivers\chromedriver.exe")
        driver.get('https://www.youtube.com/results?search_query='+"+".join(banda)+" "+"+".join(indicada))
        iniciar=driver.find_element_by_xpath('//*[@id="dismissable"]').click()
        url= driver.current_url
        driver.quit()
        sub.call('youtube-dl -f 140 '+url)
        print(i)
    return " El proceso ha terminado " 

def confirmacion(lista):

    for i in range (0,len(lista)-1):
          print(lista[i])
    return None




try:
    print("las canciones que se descargaran son : ") 
    confirmacion(obtener_Titulos1())
    s = input("desea continuar (y /n) ")
    if s == "y" : 
        os.mkdir(l)
        os.chdir(l)
        links(obtener_Titulos1())
    elif s=="n":
        print( "Qué tal suenan estos otros titulos : ")
        confirmacion(obtener_Titulos2())
        d = input("desea continuar (y /n) ")
        if d == "y" : 
            os.mkdir(l)
            os.chdir(l)
            links(obtener_Titulos2())
        else:
            print( "Hasta luego entonces")
except:
    print("revise que no haya una carpeta ya creada con este mismo nombre")
    print("revise su coneccion a internet ")
    print("intentelo de nuevo con una nueva banda o grupo musical")
    
#    print( "Algo ocurrio mal en el proceso , intentelo de nuevo con otra banda ")
#Falta adecuarlo a alexa ( hacer que salte los anuncios y pregunte cosas )y hacer un nuevo escript que recopile todos los links de internet y los descargue   

