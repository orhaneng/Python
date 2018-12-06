from Source.AssetBase import AssetBase

class Bond(AssetBase):
	'''
	Bond Asset class, inherits from AssetBase
	'''
    def __init__(self, amount, price, type= None):
        super(Bonds, self).__init__(amount, price)
        self.name = "BOND"
        self.type = type
        print("BOND created")