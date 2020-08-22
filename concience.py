# -*- coding: utf-8 -*-
"""
Created on Mon Jun 29 00:15:18 2020

@author: Felipe Valencia
"""

#importa cosas importantes
import speech_recognition as sr
import subprocess as sub
import pyttsx3 as habla
import pyautogui as gui
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from googletrans import Translator

import time
import random

#importa otros script
import emociones 
chrome_options= Options()
chrome_options.add_argument("--headless")

#chrome_options=chrome_options,



lupita = habla.init()
lupita.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
#lupita.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-ES_HELENA_11.0')
velocidad = lupita.getProperty('rate')
lupita.setProperty('rate',velocidad-25)

driver = webdriver.Chrome(chrome_options=chrome_options,executable_path=r"C:\webdrivers\chromedriver.exe")
driver.get('https://home.pandorabots.com/home.html')


def chatBot(msg):
   
    
    En_msg=traductor_en(msg)
    entrada =driver.find_element_by_xpath('//*[@id="about"]/div/div/div[2]/div[1]/textarea')
    entrada.send_keys(En_msg)
    boton= driver.find_element_by_xpath('//*[@id="send-voice-button"]')
    boton.click()
    time.sleep(2)
    response = driver.find_element_by_xpath('//*[@id="about"]/div/div/div[2]/div[3]/div/div').text
   
    respuesta = traductor_sp(str(response))    
    return respuesta

def traductor_sp(string):
   word = string
   translator = Translator(service_urls=["translate.google.com"])
   translation=translator.translate(word,dest="es")
   return translation.text

def traductor_en(lista):
   word = " ".join(lista)
   translator = Translator(service_urls=["translate.google.com"])
   translation=translator.translate(word,dest="en")
   return translation.text

def voice(habla):
    lupita.say(habla)
    lupita.runAndWait()    
    
    
    
    


while True:
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("¡ordena!")
        audio = r.listen(source)      
            
    try:    
        comando = r.recognize_google(audio,language='es-MX')
        print ("creo que dijiste "+ comando)
        comando_de_audio=comando.split(' ')
        ####################################
        adios = ('Adiós' or 'adiós') in comando_de_audio
        adios2 = ('adiós') in comando_de_audio
        que = ('Qué' or 'qué') in comando_de_audio
        quien= ('Quién' or 'quién') in comando_de_audio
        cual = ("Cúal" or 'cúal') in comando_de_audio
        te =('te'or 'tú') in comando_de_audio
        porque = ('porque') in comando_de_audio
        if adios or adios2 is True:
            voice(chatBot(comando_de_audio))
            driver.quit()
            break
        elif (que or quien or cual or te or porque) is True:
            comando_de_audio.append("?")
                        
        ####################################
        try:
            voice(emociones.emocion(comando_de_audio))
        except:
            
            voice(chatBot(comando_de_audio))
          
    except sr.UnknownValueError:
        print("no te pude entender ")
        lupita.say("Hable mas lento")
        lupita.runAndWait()
    except sr.RequestError as e : 
                print("google no dio respuesta a tu requerimiento ")
      
