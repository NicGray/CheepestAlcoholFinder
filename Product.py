class Product:
 
    def __init__(self, name, alcohol, amount, price):
        self._name = name
        self._alcohol = alcohol
        self._amount = amount
        self._price = price
        self._standardDinks = self._calcStandardDrinks()
        self._priceToDrinkRatio = self._calcPriceToDrinkRatio()

    def _calcStandardDrinks(self):
        standarDrinkAmount = 0.789
        return(self._amount/1000 * self._alcohol * standarDrinkAmount)

    def _calcPriceToDrinkRatio(self):
        return  self._standardDinks/self._price
    
    def getName(self):
        return self._name

    def getAlcoholPercentage(self):
        return self._alcohol

    def getAmount(self):
        return self._amount

    def getPrice(self):
        return self._price

    def getStandarDrinks(self):
        return self._standardDinks

    def getPricetoDrinkRatio(self):
        return self._priceToDrinkRatio
        
