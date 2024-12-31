balance = 1000
pin = 1234
wrong_turns = 1
enter_pin = int(input("Eneter PIN: "))
if enter_pin == pin:
    print(balance)
    withdraw_or_deposit = input("Would you like to withdraw or deposit? ").capitalize()
    if withdraw_or_deposit == "Withdraw":
        withdraw_amount = int(input("How much would you like to withdraw? "))
        new_withdraw_balance = balance - withdraw_amount
        print(f"Your new balance is £{new_withdraw_balance}")
    elif withdraw_or_deposit == "Deposit":
        deposit_amount = int(input("How much would you like to deposit? "))
        new_deposit_amount = balance + deposit_amount
        print(f"Your new balance is £{new_deposit_amount}")
else:
    int(input("Wrong PIN. Try again. "))
while enter_pin != pin and wrong_turns < 2:
    int(input("Wrong PIN. Try again. "))
    wrong_turns += 1
    print("Sorry. Card blocked due to wrong PIN too many times.")





