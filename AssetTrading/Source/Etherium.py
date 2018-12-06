from Source.AssetBase import AssetBase

class Etherium(Asset):
	'''
	Etherium Asset class, inherits from Asset class
	'''
    def __init__(self, amount, price):
        super(Etherium, self).__init__(amount, price)
        self.name = "ETHERIUM"
        print("ETHERIUM created")