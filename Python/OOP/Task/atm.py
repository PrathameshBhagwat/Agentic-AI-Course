class Bank_ATM:
    def __init__(self):
        self.pin = 0
        self.balance = 0

    def menu(self):
        while True:
            print("Welcome to the Bank ATM")
            print("1. Set Pin")
            print("2. Check Balance")
            print("3. Deposit Money")
            print("4. Withdraw Money")
            print("5. Update Pin")
            print("6. Exit")
        
            choice = int(input("Enter your choice: "))
        
            match choice:
                case 1:
                    self.set_pin()
                case 2:
                    self.check_balance()
                case 3:
                    self.deposit_money()
                case 4:
                    self.withdraw_money()
                case 5:
                    self.update_pin()
                case 6:
                    self.exit()
                    break
                
    def set_pin(self):
        if self.pin == 0:
            pin = int(input("Set your new Pin: "))
            self.pin = pin
            print("Pin set successfully.")
        else:
            print("Pin is already set. Please use the update option to change it.")

            
    def check_balance(self):
        pin = int(input("Enter your Pin: "))
        if pin == self.pin:
            print("Your balance is : ", self.balance)
        else:
            print("Incorrect Pin.")
        
    
    def deposit_money(self):
        pin = int(input("Enter your Pin: "))
        if pin == self.pin:
            amount = int(input("Enter amount to deposit: "))
            self.balance += amount
            print("Amount deposited successfully.")
        else:
            print("Incorrect Pin.")
    
    def withdraw_money(self):
        pin = int(input("Enter your Pin: "))
        if pin == self.pin:
            amount = int(input("Enter amount to withdraw: "))
            if amount <= self.balance:
                self.balance -= amount
                print("Your remaining balance is : ", self.balance)
                print("Amount withdrawn successfully.")
            else:
                print("Insufficient balance.")
        else:
            print("Incorrect Pin.")
    
    def update_pin(self):
        pin = int(input("Enter your current Pin: "))
        if pin == self.pin:
            new_pin = int(input("Enter your new Pin: "))
            self.pin = new_pin
            print("Pin updated successfully.")
        else:
            print("Incorrect Pin.")
            
    def exit(self):
        print("Thank you for using the ATM")            
            
            
obj = Bank_ATM()
obj.menu()