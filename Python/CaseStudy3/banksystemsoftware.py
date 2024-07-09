def bank_system():
    print("Welcome to the Bank System")
    print("1. Cash Withdraw")
    print("2. Cash Credit")
    print("3. Change Password")

    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        print("Cash Withdrawal Processed")
    elif choice == '2':
        print("Cash Credit Processed")
    elif choice == '3':
        print("Password Changed Successfully")
    else:
        print("Invalid Choice")

# Example usage:
bank_system()
