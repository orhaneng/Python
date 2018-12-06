import Customer
import AssetFactory


class TradeManagement:
    '''
    Controller for traderUI interface.  Calls the Customer and AssetFactory classes
    '''
    def __init__(self):
        self.__customerList = []

    def createCustomer(self, name, SSN, password):
        customer = Customer.Customer(name, SSN, password)
        self.__customerList.append(customer)

    def listCustomers(self):
        for item in self.__customerList:
            print(item.getName())

    def loginCustomer(self, SSN, password):
        for item in self.__customerList:
            if item.getSSN() == SSN and item.getPassword() == password:
                print("login successful")
                return True

    def deleteCustomer(self, SSN):
        for item in self.__customerList:
            if item.getSSN() == SSN:
                self.__customerList.remove(item)
                print(item.getSSN() + " deleted")
                break

    def createAccount(self, SSN, accountName, balance):
        customerId = None
        for item in self.__customerList:
            if item.getSSN() == SSN:
                item.addAccount(accountName, balance)
                break

    def customerAccountList(self, SSN):
        for item in self.__customerList:
            if item.getSSN() == SSN:
                item.listAccount()

    def buyAsset(self, SSN, accountName, assetType, amount, price):
        for item in self.__customerList:
            if item.getSSN() == SSN:
                item.buyAssetToAccount(assetType, accountName, amount, price)

    def sellAsset(self, SSN, accountName, assetType, amount, price):
        for item in self.__customerList:
            if item.getSSN() == SSN:
                item.sellAssetToAccount(assetType, accountName, amount, price)

    def withdrawMoney(self, amount, SSN, accountName):
        for item in self.__customerList:
            if item.getSSN() == SSN:
                item.withdrawMoney(amount, accountName)

    def depositMoney(self, amount, SSN, accountName):
        for item in self.__customerList:
            if item.getSSN() == SSN:
                item.depositMoney(amount, accountName)

    def getPrice(self, type):
        factoryMethod = AssetFactory.Asset()
        return factoryMethod.getPrice(str(type))
