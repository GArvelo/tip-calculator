#1. Create a greeting
print("Welcome to the tip calculator.")

#2 Create 3 var equal to.
total_bill = input("What was the total bill? ")
percentage = input("What percentage tip would you like to give? 15, 18, or 20? ")
people = input("How many people to split the bill? ")

#3 Changes those var into int and float.
money = float(total_bill)
tip = int(percentage)
split = int(people)

bill_ppl = (money * (1 + (tip / 100)) / split)
final = round(bill_ppl)

#4 Limiting floats to two decimal points with "{:.2f}".format
final = "{:.2f}".format(bill_ppl)

print(f"Each person should pay: $ {final}")