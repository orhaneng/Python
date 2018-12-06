from Source.AssetBase import AssetBase

class Currency(AssetBase):
	'''
	Currency Asset class, inherits from AssetBase class
	
	'''
    def __init__(self, amount, price, type=None):
        super(Currency, self).__init__(amount, price)
        self.name = "CURRENCY"
        self.type = type
        print("CURRENCY created")