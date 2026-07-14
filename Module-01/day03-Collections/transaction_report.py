# Read a file of telebirr transactions summarize them by customer using dictionary and handle a missing file gracefully.

# 1. read transactions.txt line by line( name, amount per line)
# 2. build a dict mapping each customer to their total spend
# 3. print each customer and total sorted highest first
# 4. wrap the file read in try/except 
# 5. write a summary to report.txt then push to Github

total_spend = {}
try:
     with open("transactions.txt", "r") as f:
          for transaction in f:
               customer, amount = transaction.split(",")
               customer = customer.strip()
               
               if customer in total_spend:
                    total_spend[customer] += int(amount)
               else:
                    total_spend[customer] = int(amount)
except FileNotFoundError:
     print("No transaction file found")

list_to_sort = []
for customer, total in total_spend.items():
     list_to_sort.append((total, customer)) 
     
sorted_list = sorted(list_to_sort, reverse=True)

for total, customer in sorted_list:
     print(f"{customer}: {total} ETB")
     

with open("report.txt", "w") as f:
     for total, customer in sorted_list:
          f.write(f"{customer}: {total} ETB\n")