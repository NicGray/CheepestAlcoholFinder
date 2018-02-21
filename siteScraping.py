import urllib.request
import re

def ReadUrl(url):
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    respData = resp.read()
    return respData
    
def DrinkType(respData):
    
