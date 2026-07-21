# Name the Big-O. For five short snippets (a list index, a single loop, a nested loop, a dict lookup, a binary search), write the Big-O of each as a comment and explain why.
animals = ["cat", "dog", "rat", "parrot", "rabbit"]
index = animals[2]    # O(1) bc it jumps directly by index
print(index)

n = 8
for i in range(0, n): 
     print(i)          # O(n) this runs 8 times

for i in range(1, 3):
     for j in range(1, 3):   
          print(i * j)
     print()                 #  O(n^2) bc inner loop executes 2 times for each of the 2 outer iterations 4 iterations of the print statement
     
d = {'a': 1}
v = d['a']          # O(1) bc we use hash table lookup





# List vs. dict lookup. Build a list and a dict of 100,000 fake account numbers. Time how long it takes to find one near the end in each
accounts = ["1000365430", "1000365431", "1000365433", "1000365434", "1000365435", "1000365436", "1000365437", "1000365438", "1000365439", "1000365440", "1000365441", "1000365442", "1000365443", "1000365444", "1000365445", "1000365446", "1000365447", "1000365448","1000365449", "1000365450"]
target = "1000365448"

for acc in accounts:
     if acc == target:
          print("Found it")

acc_dict = {"1000365430":1, "1000365431":2, "1000365433":3, "1000365434":4, "1000365435":5, "1000365436":6, "1000365437":7, "1000365438":8, "1000365439":9, "1000365440":10, "1000365441":11, "1000365442":12, "1000365443":13, "1000365444":14, "1000365445":15, "1000365446":16, "1000365447":17, "1000365448":18,"1000365449":19, "1000365450":20}
if target in acc_dict:
     print("Found in dictionary")

# Build a stack. Write a Stack class with push, pop, and peek, and use it to reverse a list of names.
class Stack:
     def __init__(self):
          self.items = []

     def push(self, item):
          self.items.append(item)

     def pop(self):
          return self.items.pop()

     def peek(self):
          return self.items[-1]

     def is_empty(self):
          return len(self.items) == 0

names = ["almaz", "abebe", "chala"]
s = Stack()
for name in names:
     s.push(name)

reversed = []
while not s.is_empty():
     reversed.append(s.pop())

print("Reversed list-", reversed)

# Build a queue. Use collections.deque to model a bank service line: enqueue five customers, then serve them in order.
from collections import deque

line = deque()
customers = ["almaz", "abebe", "chala", "beti", "sara"]

for c in customers:
     line.append(c)

while line:
     served = line.popleft()
     print("Being served now:", served)

# Singly linked list. Implement a Node and a LinkedList with push_front and a print_all() that walks the chain.
class Node:
     def __init__(self, data):
          self.data = data
          self.next = None

class LinkedList:
     def __init__(self):
          self.head = None

     def push_front(self, data):
          new_node = Node(data)
          new_node.next = self.head
          self.head = new_node

     def print_all(self):
          current = self.head
          while current:
               print(current.data, end=" ---> ")
               current = current.next
          print("None")

list = LinkedList()
list.push_front("kebede")
list.push_front("berhan")
list.push_front("abdi")
list.print_all()