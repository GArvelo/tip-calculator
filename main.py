print("Welcome to the tip calculator.")
total_bill = input("What was the total bill? ")
percentage = input("What percentage tip would you like to give? 15, 18, or 20? ")
people = input("How many people to split the bill? ")

money = float(total_bill)
tip = int(percentage)
split = int(people)

print(f"Each person should pay:{(round(money * (1+(tip/100))/split))}")