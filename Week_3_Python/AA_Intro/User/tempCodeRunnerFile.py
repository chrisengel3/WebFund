class User:
    bank_name = "Late Stage Capital"
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.account = bank_account(0.2, 0)
    
    def deposit(self, amount):
        self.account.deposit(amount)
        self.account.balance()
        return self

    def withdrawl(self, amount):
        self.account.withdrawl(amount)
        self.account.balance()
        return self

    def balance(self):
        print(self.name)
        print(self.account.balance)
        return self

    def transfer(self, receiver, amount):
        self.account_balance -= amount
        receiver.account_balance += amount
        print(f"{self.name}'s account balance is now: {self.account_balance}.")
        print(f"{receiver.name}'s account balance is now: {receiver.account_balance}.")
        return self
        
class bank_account:
    # don't forget to add some default values for these parameters!
    bank_instances = []
    def __init__(self, int_rate, account_balance): 
        self.int_rate = int_rate
        self.account_balance = account_balance
        bank_account.bank_instances.append(self)

    def deposit(self, amount):
        self.account_balance += amount
        return self

    def withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def balance(self):
        # print(self.name)
        print(self.account_balance)
        return self

    def yield_interest(self):
        if self.account_balance < 0:
            print("Insufficient Funds: Charging a $5.00 fee.")
            self.account_balance -= 5
        else:
            self.account_balance += (self.account_balance * self.int_rate)
            return self

    @classmethod
    def print_all_instances(cls):
        for value in cls.bank_instances:
            value.balance()



Chris = User("Chris Engel", "thisischrisemail@gmail.com")
Reagan = User("Reagan Shankland", "thisisreaganemail@gmail.com")
Brianna = User("Brianna Ballow", "thisisbriannaemail@gmail.com")

Chris.deposit(100).deposit(200).deposit(50).withdrawl(100).balance()
Reagan.deposit(100).deposit(200).withdrawl(50).balance()
Brianna.deposit(1000).withdrawl(50).withdrawl(50).withdrawl(50).balance()
# Chris.transfer(Brianna, 7)

# account1 = bank_account(0.2, 1000)
# account2 = bank_account(0.1, 2000)

# account1.deposit(50).deposit(55).deposit(50).withdrawl(50).yield_interest().balance()
# account2.deposit(52220).deposit(1275).withdrawl(225).withdrawl(25).withdrawl(25).withdrawl(25).yield_interest().balance()

bank_account.print_all_instances()