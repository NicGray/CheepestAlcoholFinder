import urllib.request
import re

#get site contents
def ReadUrl(url):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    return respData
#--------------------------

#get type of drink from url    
def DrinkType(url):    
    typeText = re.findall('com.au/([A-Za-z %20]+)/',str(url))
    return typeText[0]
#--------------------------

#get informatiopn of beer type drinks
def BeerInfo(respData):
    name = GetName(respData)
    alcohol = GetAlcohol(respData)    
    amount = re.findall('([0-9]+ x [0-9]+)mL',str(respData))
    return [name,alcohol,int(amount[0])]
#--------------------------

#get information on wine type drinks
def WineInfo(respData):
    name = GetName(respData)
    alcohol = GetAlcohol(respData)  
    amount = re.findall(' ([0-9]+)mL</li',str(respData))
    print(amount)
    return [name, alcohol, int(amount[0])]
#--------------------------

#returns name of product
def GetName(respData):
    name = re.findall('>([A-Za-z0-9 \(\)&]+)</li',str(respData))
    return name[0]
#--------------------------

#returns alchohol of product as float
def GetAlcohol(respData):
    alcohol = re.findall('>([0-9.]+)%</td',str(respData))
    return float(alcohol[0])
#--------------------------
