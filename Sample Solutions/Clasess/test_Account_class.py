from Account_class import Account #python 3 onwards

cust1 = Account("smith", "12345455", "05-12-34")
cust1.deposit(200)
cust1.get_balance()


cust2 = Account("George", "12345466", "65-14-34")
cust2.deposit(200)
cust2.withdraw(4000)  #test for raised exception
cust2.get_balance()


