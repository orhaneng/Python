from Source.AssetBase import AssetBase

class Ripple(Asset):
	'''
	Ripple Asset class, inherits from Asset
	'''
    def __init__(self, amount, price):
        super(Ripple, self).__init__(amount, price)
        self.name = "RIPPLE"
        print("RIPPLE created")