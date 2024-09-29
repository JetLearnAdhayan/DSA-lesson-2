class Bank:
    def __init__(self, person, amount, accountnumber):
        self.person=person
        self.amount =amount
        self.accountnumber = accountnumber

    def displayDeatais(self):
        print("Name: {}, Balance: {}, account no : {}".format(self.person,self.amount,self.accountnumber))

            
#child class
class Login(Bank):
    def __init__(self, person, amount, accountnumber, password):
        Bank.__init__(self, person,amount, accountnumber)
        self.password=password
    def displayDeatails(self):
        print("Name: {}, Balance: {}, account no : {}, password {}".format(self.person,self.amount,self.accountnumber,self.password)) 
    


Login = Login("Adhayan", "10000", "324567876543","123456")

Login.displayDeatails()