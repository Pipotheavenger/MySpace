# -*- coding: utf-8 -*-
"""
Created on Thu Jun 25 20:51:48 2020

@author: Felipe Valencia
"""
import speech_recognition as sr
import subprocess as sub
import pyttsx3 as habla
import pyautogui as gui
import climate
import time
import random




lupita = habla.init()
lupita.setProperty('voice', 'HKEY_LOCAL_MACHINE\SOFTWARE\Microsoft\Speech\Voices\Tokens\TTS_MS_ES-MX_SABINA_11.0')
velocidad = lupita.getProperty('rate')
lupita.setProperty('rate',velocidad-25)
   

 
    
def interpretar(comando_de_audio):
    comando_de_audio = comando_de_audio.split(' ')
    #validaciones de comando 
    nombre = ('Zara' or 'sara') in comando_de_audio
    ver_video=('video') in comando_de_audio
    escribir=('escribir' or 'texto') in comando_de_audio
    clima = ('clima') in comando_de_audio
    google = ('Dime') in comando_de_audio
    google2= ('dime') in comando_de_audio
   
    #Que hacer si 
  
    if nombre is True :
        decirnombre()
    elif ver_video is True :
        abrir_youtube()
    elif escribir is True: 
        abrir_blockNotas()
    elif clima is True : 
        decir_clima()
    elif (google or google2) is True : 
        comando_de_audio.pop(0)
        a=climate.google(comando_de_audio)
        lupita.say(a)
        lupita.runAndWait()
 
def decir_clima():
    lupita.say(climate.climateHoy())
    lupita.runAndWait()
 
def decirnombre():
    
    saludo=["Buenos dias señor","que gusto verlo de nuevo","Cómo está señor", "A sus ordenes" , "Aquí estoy"]
   
    p= random.randint(0,len(saludo)-1)
    lupita.say(saludo[p])
    lupita.runAndWait()
def abrir_youtube():
    sub.call('start https://www.youtube.com/?gl=CO&hl=es-419' ,shell=True)
    return None
def abrir_blockNotas():
    lupita.say("chulazo")
    lupita.runAndWait()
    sub.call('start notepad.exe',shell=True)
    time.sleep(1.5)
    gui.write('dictame papasito')

def despedida():
    
    global verdad
    verdad = False        
 
verdad = True 
while verdad ==True:
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("¡ordena!")
        audio = r.listen(source)      
            
    try:    
        comando = r.recognize_google(audio,language='es-MX')
        print ("creo que dijiste "+ comando )
        despedida=('Adiós' or ('adiós')) in comando
        if despedida is True:
            desp=["Adios","Nos vemos","hasta pronto","Hasta siempre","Te veo luego","Cuídate","Nos vemos luego"]
            l=random.randint(0,len(desp)-1)
            lupita.say(desp[l])
            lupita.runAndWait()
            break
        interpretar(comando)
          
    except sr.UnknownValueError:
        print("no te pude entender ")
        lupita.say("Hable mas lento")
        lupita.runAndWait()
    except sr.RequestError as e : 
                print("google no dio respuesta a tu requerimiento ")
      