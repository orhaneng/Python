import random
import Account
import AssetFactory


class Customer:
    '''
    Customer controller class

    Initialization
    str : name
    str : SSN
    int : id
    list str: accountList
    str : password
    '''
    def __init__(self, name, SSN, password):
        self.__name = name
        self.__SSN = SSN
        self.__id = random.randint(1, 999999)
        self.__accountList = []
        self.__password = password
        print("Customer has created. name:" + name + " customerID:" + str(self.__id))

    def changePersonalInfo(self, password):
        self.__password = password
        print("password changed")

    def addAccount(self, accountName, balance):
        self.__accountList.append(Account.Account(self.__id, accountName, balance))

    def listAccount(self):
        for item in self.__accountList:
            print(item.getInfo())

    def buyAssetToAccount(self, assetType, accountName, amount, price):
        for item in self.__accountList:
            if item.getName() == accountName:
                factoryMethod = AssetFactory.Asset()
                item.addAsset(factoryMethod.buyAsset(str(assetType), amount, price))

    def sellAssetToAccount(self, assetType, accountName, amount, price):
        for item in self.__accountList:
            if item.getName() == accountName:
                for item2 in item.getAssetList():
                    if item2.name == assetType:
                        if (int(item2.getAmount()) - int(amount) < 0):
                            print("insufficent asset amount")
                        else:
                            item2.setAmount(int(item2.getAmount()) - int(amount))
                            self.depositMoney(amount, accountName)

    def withdrawMoney(self, amount, accountName):
        for item in self.__accountList:
            if item.getName() == accountName:
                item.withdrawMoney(amount)

    def depositMoney(self, amount, accountName):
        for item in self.__accountList:
            if item.getName() == accountName:
                item.depositMoney(amount)

    def getSSN(self):
        return self.__SSN

    def getId(self):
        return self.__id

    def getName(self):
        return self.__name

    def getPassword(self):
        return self.__password
