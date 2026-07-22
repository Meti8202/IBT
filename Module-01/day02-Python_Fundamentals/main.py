# Write a small Python program that splits a restaurant bill with its eats across friends using variables operators a function and a loop 

# 1. Store bill total(ETB) and number of people in variables
# 2. Write a  function split_bill(total, people, tip_rate=0.10)
# 3. Use it to compute the per_person amount, tip included
# 4. Loop over a list of names and print each person's share
# 5. Commit and push your day02 folder to Github

total = 3000
people = 3

def split_bill(total, people, tip_rate=0.10):
     tip_amount = total * tip_rate
     total_bill = total + tip_amount
     share_per_person = total_bill / people
     return share_per_person

# print(split_bill(total, people))
share_per_person = split_bill(total, people)

friends = ["Beti", "Chala", "Aster"]

for person in friends:
     print(f"{person} pays {share_per_person} ETB")