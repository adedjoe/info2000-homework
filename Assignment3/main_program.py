from bankutils import BankAccount, SavingsAccount

def test_bank_account():
    print("\n--- BankAccount Test Cases ---")
    
    # Test case 1: Negative initial balance
    try:
        account = BankAccount(-100)
    except ValueError as e:
        print(f"Test complete: {e}")
    
    # Test case 2: Valid operations
    account = BankAccount(100)
    print(f"Initial balance: {account}")
    
    # Deposit tests
    print(account.deposit(50))
    print(f"After deposit: {account}")  # Expected balance: $150
    print(account.deposit(-20))  # Expected error message
    
    # Withdraw tests
    print(account.withdraw(200))  # Expected: "Insufficient balance"
    print(account.withdraw(100))
    print(f"After withdrawal: {account}")  # Expected balance: $50
    print(account.withdraw(-30))  # Expected error message
    
    # Check balance test
    print(f"Current balance: ${account.check_balance()}")


def test_savings_account():
    print("\n--- SavingsAccount Test Cases ---")
    
    # Test case 1: Create savings account with 5% interest
    savings = SavingsAccount(200, 0.05)
    print(f"Initial savings: {savings}")
    
    # Deposit test
    print(savings.deposit(100))
    print(f"After deposit: {savings}")  # Expected balance: $300
    
    # Apply interest test
    print(savings.apply_interest())  # 5% interest on $300
    print(f"After applying interest: {savings}")  # Expected: $315
    
    # Withdraw test
    print(savings.withdraw(50))
    print(f"After withdrawal: {savings}")  # Expected: $265
    
    # Check balance test
    print(f"Current balance: ${savings.check_balance()}")
    
    # Second interest application
    print(savings.apply_interest())
    print(f"After second interest: {savings}")  # Expected: $278.25


if __name__ == "__main__":
    print("This is a Bank Account Testing Program") 
    test_bank_account()
    test_savings_account()
    