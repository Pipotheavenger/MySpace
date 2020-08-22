# -*- coding: utf-8 -*-
"""
Created on Sun Jun 21 23:16:26 2020

@author: Felipe Valencia
"""

import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime
import time

URL= 'https://www.amazon.com/-/es/Canon-Frame-Digital-Camera-24-105mm/dp/B01KURGS9Y/ref=sxin_7_ac_d_pm?__mk_es_US=%C3%85M%C3%85%C5%BD%C3%95%C3%91&ac_md=9-3-TcOhcyBkZSBVUyQyLDIwMA%3D%3D-ac_d_pm&cv_ct_cx=camara+canon&dchild=1&keywords=camera+canon&pd_rd_i=B01KURGS9Y&pd_rd_r=e6e92079-8aee-45f0-b18a-2f219086712b&pd_rd_w=rVHcz&pd_rd_wg=t4WKg&pf_rd_p=08938f36-417a-4302-bc9c-c25b93012e7d&pf_rd_r=DWBKR579DAY7VA4F7736&psc=1&qid=1592799468&s=videogames-intl-ship&sr=1-4-22d05c05-1231-4126-b7c4-3e7a9c0027d0'

headers = {"user-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36'}

x = []
y = []


def check_price():
    try:
    
     
        page = requests.get(URL,headers=headers)
        
        soup = BeautifulSoup(page.content , 'html.parser')
        
        
        
        price = soup.find(id ="priceblock_saleprice").get_text()
        point= price.find(".")
        precio_converted = price[4:point]
        dot_price = precio_converted.replace(',','.')
        precio=float(dot_price)
       
       
        data = x.append(precio)
        now = y.append(str(datetime.now().day) +" de " + str(datetime.now().month))
        
        if (precio < 3 ):
            send_email()          
    except:
        print("Merd")
        check_price()
        
        
def send_email():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('pipesuperheroe@gmail.com','lbbdrkwjxnwhtsrf')
    subject=" Un nuevo producto ha bajado de precio !"
    body = ("el precio del producto de interes ha caido , checalo tu mismo : " + str(URL))
    msg = f"Subject: {subject}\n\n{body}"
    server.sendmail(
        'pipesuperheroe@gmail.com',
        'gavalenciap.procometales@gmail.com',
        msg
        )
    print("email send succesfully ")
    server.quit()

check_price()
 

#FALTA PROBAR QUE FUNCIONA , GRAFICAR LAS LISTAS Y PONERLE UNA PAGINA QUE VALGA LA PENA 
    