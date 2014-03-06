# The Stock class
# Author: Brian Hamburg

# define Stock class
class Stock:
    def __init__(self, name, symbol, previousClosingPrice, currentPrice):
        self.__name = name
        self.__symbol = symbol
        self.__previousClosingPrice = previousClosingPrice
        self.__currentPrice = currentPrice

    def getName(self):
        return self.__name 

    def getSymbol(self):
        return self.__symbol

    def getpreviousClosingPrice(self):
        return self.__previousClosingPrice

    def getCurrentPrice(self):
        return self.__currentPrice

    def setpreviousClosingPrice(self, previousClosingPrice):
        self.__previousClosingPrice = previousClosingPrice

    def setCurrentPrice(self, currentPrice):
        self.__currentPrice = currentPrice

    def getHeight(self):
        return self.height

    def getChangePercent(self):
        return format((self.__currentPrice - self.__previousClosingPrice) * 100 / self.__previousClosingPrice, "5.2f") + "%"

def main():
    # call Stock class and print results
    stock = Stock("Intel", "INTC", 20.5, 20.35)
    print("The price change is", stock.getChangePercent())
          
main()
