class BankAccount:
    def __init__(self, initial_balance):
        if initial_balance < 0:
            print("Error: Initial balance cannot be negative")
            self.balance = 0 
        else:
            self.balance = initial_balance
    
    def deposit(self, amount):
        if amount <= 0:
            return "Error: Deposit amount must be positive"
        self.balance += amount
        return str(amount) + " deposited successfully"
    
    def withdraw(self, amount):
        if amount <= 0:
            return "Error: Withdrawal amount must be positive"
        if amount > self.balance:
            return "Error: Insufficient balance"
        self.balance -= amount
        return str(amount) + " withdrawn successfully"
    
    def check_balance(self):
        return self.balance
    
    def __str__(self):
        return "Bank Account Balance: $" + str(self.balance)


class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0, interest_rate=0.02):
        BankAccount.__init__(self, initial_balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return "Interest applied: $" + str(round(interest, 2))
    
    def __str__(self):
        return "Savings Account Balance: $" + str(self.balance) + ", Interest Rate: " + str(self.interest_rate*100) + "%"