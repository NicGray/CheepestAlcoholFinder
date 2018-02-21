import siteScraping as SS
from Product import Product
#wine
#url = "https://www.liquorland.com.au/White%20Wine/counting-sheep-marlborough-sauv-blanc-750ml_7805494"

#cider
#url = "https://www.liquorland.com.au/Beer/somersby-apple-cider-can-375ml-10-pack-_1253180"

#beer
url = "https://www.liquorland.com.au/Beer/hahn-premium-light-bottle-375ml_380713"
url = "https://www.liquorland.com.au/Beer/xxxx-gold-block-can-375ml_6577554"

respData = SS.readUrl(url)

drinkType = SS.drinkType(url)

if drinkType == "Beer":
    info = SS.beerInfo(respData)
    test = Product(info[0],info[1],info[2], info[3])
    print(test.getPricetoDrinkRatio())
elif drinkType == "White%20Wine":
    info= SS.wineInfo(respData)
    test = Product(info[0],info[1],info[2], info[3])
    print(test.getPricetoDrinkRatio())

