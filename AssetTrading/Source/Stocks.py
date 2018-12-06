from Source.AssetBase import AssetBase

class Stocks(AssetBase):
	'''
	Stock Asset class, inherits from AssetBase class
	
	'''
    stockCode =""

    def __init__(self, amount, price):
        super(Stocks, self).__init__(amount, price)
        self.name = "STOCK"
        print("STOCK created")
