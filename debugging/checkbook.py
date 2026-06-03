#!/usr/bin/python3

class Checkbook:
    """
    A class to manage a simple personal checkbook.
    """
    def __init__(self):
        """
        Initializes the checkbook with a zero balance.
        """
        self.balance = 0.0

    def deposit(self, amount):
        """
        Adds a specified amount to the balance.
        
        Parameters:
        amount (float): The amount of money to deposit.
        """
        self.balance += amount
        print("Deposited ${:.2f}".format(amount))
        print("Current Balance: ${:.2f}".format(self.balance))

    def withdraw(self, amount):
        """
        Deducts a specified amount from the balance if funds are sufficient.
        
        Parameters:
        amount (float): The amount of money to withdraw.
        """
        if amount > self.balance:
            print("Insufficient funds to complete the withdrawal.")
        else:
            self.balance -= amount
            print("Withdrew ${:.2f}".format(amount))
            print("Current Balance: ${:.2f}".format(self.balance))

    def get_balance(self):
        """
        Displays the current balance of the checkbook.
        """
        print("Current Balance: ${:.2f}".format(self.balance))

def main():
    """
    Main function to interact with the Checkbook class via command line.
    Includes error handling for non-numeric inputs.
    """
    cb = Checkbook()
    while True:
        action = input("What would you like to do? (deposit, withdraw, balance, exit): ")
        if action.lower() == 'exit':
            break
        elif action.lower() == 'deposit':
            try:
                amount_input = input("Enter the amount to deposit: $")
                amount = float(amount_input)
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")
        elif action.lower() == 'withdraw':
            try:
                amount_input = input("Enter the amount to withdraw: $")
                amount = float(amount_input)
                if amount < 0:
                    print("Amount must be positive.")
                else:
                    cb.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value for the amount.")
        elif action.lower() == 'balance':
            cb.get_balance()
        else:
            print("Invalid command. Please try again.")

if __name__ == "__main__":
    main()
