import random

# I, Jay Patel, 000881881, certify that this work is my own effort and that I have not allowed anyone else to copy from it.
# ----assignment 2, question 2----

# Generate a random transaction amount between 1 and 1000, including cents.
amount = random.randint(1, 1000) + round(random.randint(0, 100) / 100, 2)

# Display the transaction amount.
print("Your transaction amount is $" + "{:.2f}".format(amount))

# Prompt the user to enter the payment amount with 2 decimals.
payment = float(input("Enter the payment amount with 2 decimals: "))

# Calculate the change.
change = payment - amount

if change <= 0:
    print("No change owed")
else:
    # Calculate the number of dollars, quarters, dimes, and nickels
    dollars = int(change)
    change -= dollars

    quarters = int(change / 0.25)
    change -= quarters * 0.25

    dimes = int(change / 0.10)
    change -= dimes * 0.10

    nickels = int(change + round(change * 2, 1) * 10)

    # Display the change breakdown
    print("You will receive:")
    print(f"{dollars} dollars, {quarters} quarters, {dimes} dimes, and {nickels} nickels in change.")
