# Checking account class
class CheckingAccount:
    def __init__(self, firstName, lastName, address, accountNumber, email):
        self.firstName = firstName
        self.lastName = lastName
        self.address = address
        self.accountNumber = accountNumber
        self.__balance = 0 # Private Attribute
        self.email = email
    # Method to credit funds to Checking Account
    def creditFunds(self, ammount):
        self.__balance += ammount
    # Method to debit funds to Checking Account
    def debitFunds(self, ammount):
        self.__balance -= ammount
    # Method to dispay funds in Checking Account
    def getBalance(self):
        return self.__balance