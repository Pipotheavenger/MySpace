# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 19:57:58 2020

@author: Felipe Valencia
"""
#Aqui se escribiran solo las emociones del robot , es decir como sus saludos e informacion mas humana. 

import random


def emocion(comand):

  
    #validaciones de comando 
    nombre = ('Zara' or 'sara') in comand
    bien = ('bien') in comand
   
    #Que hacer si 
  
    if nombre is True:
         saludo=["Buenos dias señor","que gusto verlo de nuevo","Cómo está señor", "A sus ordenes" , "Aquí estoy"]
         rand=random.randint(0,len(saludo)-1)
         get=saludo[rand]
         return str(get)
        
    elif bien is True : 
       howru=["me alegra escuchar eso","que gusto me da","eso supongo que es bueno ", "pero que gran noticia" , "tambien estoy bien , por si le interesa"]
       rand=random.randint(0,len(howru)-1)
       get=howru[rand]
       return str(get)
    raise
    
    
       
