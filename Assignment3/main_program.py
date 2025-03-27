from bankutils import BankAccount, SavingsAccount

if __name__ == "__main__":
    print("\n--- BankAccount Test Cases ---")
    
    # Test case 1: Negative initial balance
    account = BankAccount(-100)  # should print error message

    # Test case 2: Valid operations
    account = BankAccount(100)
    print("Initial balance:", account)
    
    # Deposit tests
    print(account.deposit(50))
    print("After deposit:", account)  # Expected balance: $150
    print(account.deposit(-20))  # Expected error message
    
    # Withdraw tests
    print(account.withdraw(200))  # Expected: "Insufficient balance"
    print(account.withdraw(100))
    print("After withdrawal:", account)  # Expected balance: $50
    
    # Check balance test
    print("Current balance: $" + str(account.check_balance()))



    print("\n--- SavingsAccount Test Cases ---")
    
    # Test case 1: Create savings account with 5% interest
    savings = SavingsAccount(200, 0.05)
    print("Initial savings:", savings)
    
    # Deposit test
    print(savings.deposit(100))
    print("After deposit:", savings)  # Expected balance: $300
    
    # Apply interest test
    print(savings.apply_interest())  # 5% interest on $300
    print("After applying interest:", savings)  # Expected: $315
    
    # Withdraw test
    print(savings.withdraw(50))
    print("After withdrawal:", savings)  # Expected: $265
    
    # Check balance test
    print("Current balance: $" + str(savings.check_balance()))



