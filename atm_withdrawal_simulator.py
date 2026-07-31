BALANCE = 500

withdraw_amount = int(input("How much money do you you want to withdraw?: "))

if withdraw_amount <= BALANCE:
    remaining_balance = BALANCE - withdraw_amount
    print(f"Withdrawal successful! Remaining balance: R{remaining_balance}")

elif withdraw_amount <= 0 :
    print("Invalid amount. You must withdraw  more than R0.")

else:
    print("Declined. Insufficient funds.")