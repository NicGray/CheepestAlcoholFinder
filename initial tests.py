import urllib.request
import re
import siteScraping as SS
#wine
#url = "https://www.liquorland.com.au/Sparkling/moet-chandon-brut-imperial-nv-piccolo-200ml_5682407"

#cider
#url = "https://www.liquorland.com.au/Beer/somersby-apple-cider-can-375ml-10-pack-_1253180"

#beer
url = "https://www.liquorland.com.au/Beer/hahn-premium-light-bottle-375ml_380713"


respData = SS.ReadUrl(url)

drinkType = ss.DrinkType(respData)

#name of drank

name = re.findall('>([A-Za-z0-9 \(\)&]+)</li',str(respData))

#alcohol percentage

alcohol = re.findall('>([0-9.%]+)</td',str(respData))

#liquid in case
liquidCase = re.findall('([0-9]+ x [0-9]+)mL',str(respData))
liquidCase = liquidCase[0]
print(name, alcohol, liquidCase)


