import bankaccount

def main():
    start_bal = float(input("Enter your starting balance: "))

    savings = bankaccount.BankAccount(start_bal)

    pay = float(input("How much were you paid this week? " ))
    print("I will deposit that into your account.")
    savings.deposit(pay)

    print("Your account balance is $",
          format(savings.get_balance(), ",.2f"),
          sep=" ")

    cash = float(input("How much would you like to withdraw? "))
    print("I will withdraw that from your account")
    savings.withdraw(cash)

    print("Your account balance is $",
          format(savings.get_balance(), ",.2f"),
          sep=" ")
main()
