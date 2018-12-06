import TradeManagement

trade = TradeManagement.TradeManagement()
'''
Test File, tests creation of classes
'''


# customer transactions
trade.createCustomer("john", "12345","1")
trade.createCustomer("Evan", "44444","1")
trade.createCustomer("Kirk", "55555","1")
trade.deleteCustomer("55555")
trade.listCustomers()

# account transactions
trade.createAccount("44444", "ElephantAccount", 0.0)
trade.createAccount("44444", "LionAccount", 0.0)

# asset transactions
trade.buyAsset("44444", "ElephantAccount", "BITCOIN", 100, 6300)
trade.buyAsset("44444", "ElephantAccount", "CURRENCY", 90, 1.4)
trade.buyAsset("44444", "LionAccount", "CURRENCY", 100, 1.7)
trade.customerAccountList("44444")
trade.sellAsset("44444", "LionAccount", "CURRENCY", 50, 1.7)
trade.customerAccountList("44444")

# withdraw deposit money
trade.depositMoney(90000, "44444", "ElephantAccount")
trade.customerAccountList("44444")
trade.withdrawMoney(10000, "44444", "ElephantAccount")
trade.customerAccountList("44444")
