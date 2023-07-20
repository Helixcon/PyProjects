class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, account_number, name, initial_balance=0):
        if account_number in self.accounts:
            print("Account number already exists.")
            return False

        if initial_balance < 0:
            print("Initial balance cannot be negative.")
            return False

        self.accounts[account_number] = {
            "name": name,
            "balance": initial_balance
        }
        print("Account created successfully.")
        return True

    def deposit(self, account_number, amount):
        if account_number not in self.accounts:
            print("Account not found.")
            return False

        if amount <= 0:
            print("Invalid amount.")
            return False

        self.accounts[account_number]["balance"] += amount
        print("Deposit successful.")
        return True

    def withdraw(self, account_number, amount):
        if account_number not in self.accounts:
            print("Account not found.")
            return False

        if amount <= 0 or amount > self.accounts[account_number]["balance"]:
            print("Invalid amount.")
            return False

        self.accounts[account_number]["balance"] -= amount
        print("Withdrawal successful.")
        return True

    def check_balance(self, account_number):
        if account_number not in self.accounts:
            print("Account not found.")
            return False

        balance = self.accounts[account_number]["balance"]
        print(f"Balance: {balance}")
        return balance


def main():
    bank = Bank()

    while True:
        print("\nBanking System Menu:")
        print("1. Create Account")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Check Balance")
        print("5. Exit")

        choice = input("Enter your choice (1/2/3/4/5): ")

        if choice == '1':
            account_number = input("Enter account number: ")
            name = input("Enter account holder's name: ")
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(account_number, name, initial_balance)
        elif choice == '2':
            account_number = input("Enter account number: ")
            amount = float(input("Enter the deposit amount: "))
            bank.deposit(account_number, amount)
        elif choice == '3':
            account_number = input("Enter account number: ")
            amount = float(input("Enter the withdrawal amount: "))
            bank.withdraw(account_number, amount)
        elif choice == '4':
            account_number = input("Enter account number: ")
            bank.check_balance(account_number)
        elif choice == '5':
            print("Exiting the Banking System.")
            break
        else:
            print("Invalid choice. Please enter a valid option (1/2/3/4/5).")


if __name__ == "__main__":
    main()

