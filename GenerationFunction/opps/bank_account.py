class bank_account:
    def __init__(self,balence):
        self.__balence=balence
    def deposite(self,amount):
        self.__balence+=amount
    def withdraw(self,amount):
        if amount<=self.__balence:
            self.__balence-=amount
        else:
            print("balence is low")
    def get_balence(self):
        return self.__balence
pawan=bank_account(1000)
print(pawan.get_balence())
pawan.deposite(4512)
print(pawan.get_balence())
pawan.deposite(2000)
print(pawan.get_balence())
print(pawan.withdraw(1000))
#print(pawan.withdraw())
