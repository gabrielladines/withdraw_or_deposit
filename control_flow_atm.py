balance = 1000
pin = 1234
pin_attempts = 1
enter_pin = int(input("Eneter PIN: "))
while enter_pin != pin:
    enter_pin = int(input("Wrong PIN. Try again. "))
    pin_attempts += 1
    if pin_attempts == 3:
        print("Card has been blocked due to too many wrong attempts.")   
        break
if enter_pin == pin:
    print(f"Your balance is: £{balance}")
    withdraw_or_deposit = input("Would you like to withdraw or deposit? ").capitalize()
    if withdraw_or_deposit == "Withdraw":
        withdraw_amount = int(input("How much would you like to withdraw? "))
        if withdraw_amount > balance:
            new_withdraw_amount = int(input(f"Not enough funds. Please select amount less than or equal to £{balance}. "))
            balance -= new_withdraw_amount
            print(f"Your new balance is £{balance}")
        else:
            balance -= withdraw_amount
            print(f"Your new balance is £{balance}")    
    elif withdraw_or_deposit == "Deposit":
        deposit_amount = int(input("How much would you like to deposit? "))
        balance += deposit_amount
        print(f"Your new balance is £{balance}")
