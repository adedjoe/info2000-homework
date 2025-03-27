class BankAccount:
    def __init__(self, initial_balance=0):
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative")
        self.balance = initial_balance
    
    def deposit(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Deposit amount must be positive")
            self.balance += amount
            return f"${amount} deposited successfully"
        except ValueError as e:
            return str(e)
    
    def withdraw(self, amount):
        try:
            if amount <= 0:
                raise ValueError("Withdrawal amount must be positive")
            if amount > self.balance:
                raise ValueError("Insufficient balance")
            self.balance -= amount
            return f"${amount} withdrawn successfully"
        except ValueError as e:
            return str(e)
    
    def check_balance(self):
        return self.balance
    
    def __str__(self):
        return f"Bank Account Balance: ${self.balance}"


class SavingsAccount(BankAccount):
    def __init__(self, initial_balance=0, interest_rate=0.02):
        super().__init__(initial_balance)
        self.interest_rate = interest_rate
    
    def apply_interest(self):
        interest = self.balance * self.interest_rate
        self.balance += interest
        return f"Interest applied: ${interest:.2f}"
    
    def __str__(self):
        return f"Savings Account Balance: ${self.balance}, Interest Rate: {self.interest_rate*100}%"