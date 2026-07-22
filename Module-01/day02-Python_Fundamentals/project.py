# What you will build
# A program customer_report.py that takes a list of customers (name and TeleBirr balance in ETB), assigns each a tier, and prints a tidy report — plus a summary count of how many customers fall in each tier.
# Requirements
#  Store at least five customers as a list of (name, balance) pairs.
#  Write a function tier(balance) that returns "Premium" (≥ 1000), "Standard" (≥ 500), or "Basic" (below 500).
#  Loop over the customers and print one line each: name, tier, and balance in ETB.
#  After the loop, print how many customers are in each tier

customers = [
     ("Dagim", 12500),
     ("Meklit", 800),
     ("Feven", 6079),
     ("Beti", 350),
     ("Almaz", 855),
     ("Kebede", 724),
     ("Nati", 501),
     ("Sami", 101 ),
     ("Abebe", 616 ),
     ("Beti", 2000),
     ("Abel", 995),
]

def tier(balance):
     if balance >= 1000:
          return "Premium"
     elif balance >= 500:
          return "Standard"
     return "Basic"



counter = {}
for name, balance in customers:
     print(f"{name}: {tier(balance)} ({balance} ETB)")     
     tier_count = tier(balance)              
     if tier_count in counter:
          counter[tier_count] += 1
     else:
          counter[tier_count] = 1    

print("Total number of tiers: ", counter)

          