# Unique cities. Given a list with repeated city names, use a set to print the distinct cities, then the count.
cities= set(("Paris", "Seoul", "Malta","Houston", "Moscow ", "Delhi","Lagos", "Tokyo", "London","Delhi", "Addis Ababa", "Dubai","Toronto", "Delhi", "Berlin","Madrid", "Athens", "Antalya","Baku", "Amsterdam", "London","Moscow ", "Sydney ", "Baku"))

print(cities)
print(len(cities))

# Price report. Make a dictionary of five grocery items and prices in ETB. Loop with .items() to print each on its own line.
shopping_list = { "Bread": 20, "Tomato": 60, "Onion": 65, "Potato": 50, "Pepsi": 70 }

for item in shopping_list.items():
     print(item)

# Tax comprehension. Given prices = [100, 250, 400, 80], use one comprehension to build a list with 15% tax added.
prices = [100, 250, 400, 80]
tax_added = [val + (val * 0.15) for val in prices ]
print(tax_added)

# Cheap items. From the same list, use a comprehension with a condition to keep only prices under 200.
prices = [100, 250, 400, 80]
cheap_items = [val for val in prices if val < 200] 
print(cheap_items)

# Write & read. Write three customer names to names.txt, then open it and print each name back, one per line.
with open("names.txt", "w") as f:
     f.write("Trinity\n")
     f.write("Aniya\n")
     f.write("Melanie\n")
with open("names.txt", "r") as f:
     for name in f:
          print(name.strip())

# Safe division. Ask the user for a number and divide 1000 by it, catching both ValueError and ZeroDivisionError.
try:
     number = int(input("Enter a number: "))
     result = 1000 /number
     # print(result)
except ValueError:
     print("Please enter a number!")
except ZeroDivisionError:
     print("Can't be zero")
else:
     print(result)
