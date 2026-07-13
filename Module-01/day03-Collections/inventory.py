# What you will build
# A program inventory.py for a small Addis Ababa pharmacy that loads stock from a file into a dictionary, lets you update quantities, reports low-stock items, and saves the updated stock back to the file.
# Requirements
#  Read stock.txt (one item,quantity per line) into a dictionary, inside a try / except for a missing file.
#  Add a function that increases or decreases an item's quantity by a given amount.
#  Use a comprehension or loop to print every item where the quantity is below 10 (low stock).
#  Write the updated dictionary back to stock.txt so the changes persist.

stock = {}
try:
    with open("stock.txt", "r") as f:
        for item in f:
            # print(item.split())
            medicine, quantity = item.replace(",", " ").split()
            stock[medicine] = int(quantity)
except FileNotFoundError:
    print("File not found.")
# print(stock)

def stock_up(medicine, amount):
    if medicine not in stock:
        stock[medicine] = 0
    stock[medicine] = stock[medicine] + amount

stock_up("Paracetamol", 35)
stock_up("Multivitamin", -5)
stock_up("Aspirin", 5)
stock_up("Amoxicillin", 20)
print(stock)

low_stock = [medicine for medicine, quantity in stock.items() if quantity < 10]
print(low_stock)

with open("stock.txt", "w") as f:
    for medicine, quantity in stock.items():
        update = f"{medicine},{quantity}\n"
        f.write(update)
