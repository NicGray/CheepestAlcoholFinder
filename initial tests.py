import urllib.request
import re
import siteScraping as SS
#wine
url = "https://www.liquorland.com.au/White%20Wine/counting-sheep-marlborough-sauv-blanc-750ml_7805494"

#cider
#url = "https://www.liquorland.com.au/Beer/somersby-apple-cider-can-375ml-10-pack-_1253180"

#beer
#url = "https://www.liquorland.com.au/Beer/hahn-premium-light-bottle-375ml_380713"


respData = SS.ReadUrl(url)

drinkType = SS.DrinkType(url)

if drinkType == "Beer":
    print(SS.BeerInfo(respData))
elif drinkType == "White%20Wine":
    print(SS.WineInfo(respData))


