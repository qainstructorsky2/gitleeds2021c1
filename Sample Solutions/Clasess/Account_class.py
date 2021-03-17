class Account:
    bank ="rbs" #class variable

    def __init__(self,name,account_no,sort_code): # constructor

        self.name=name
        self.account_no =account_no
        self.sort_code =sort_code
        self.balance=0


    #Function to get balance

    def get_balance(self):
        print("\n Available Balance=", self.balance)

    # Function to withdraw cash - without custom exceptions
    #def  withdraw_cash(self):
     #   amount = float(input("Enter amount to be Withdrawn: "))
     #   if self.balance >= amount:
     #       self.balance -= amount
     #      print("\n You Withdrew:", amount)
     #  else:
     #      print("\n Insufficient balance  ")

    # Function to withdraw cash - custom exceptions
    def  withdraw_cash(self):
      amount = float(input("Enter amount to be Withdrawn: "))
      if self.balance >= amount:
         self.balance -= amount


    def withdraw(self, amount):
        self.check_amount(amount)
        # Raise a custom exception when there is insufficient balance.
        try:
            if amount > self.balance:
            raise InsufficientBalanceException('Insufficient balance')
        except:
            self.balance -= amount

        finally:
        pass #normally close DB connections or files




    # Function to deposit amount
    def deposit(self, amount):
        amount = float(input("Enter amount to be deposited: "))
        self.balance += amount
        print("\n Amount Deposited:", amount)








