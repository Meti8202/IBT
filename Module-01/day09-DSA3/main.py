# Goal
# Model the bank's branch hierarchy as a tree with a recursive total, and its transfers as a graph you can traverse with BFS.
# Steps
# Copy day08/registry.py into day09/ to keep growing it.
# Build a Branch tree: head office → regions → branches.
# Write a recursive total_balance() for any branch.
# Build a transfers graph as a dict, and a bfs() over it.
# Print the bank's total and who CBE-1 can reach; push to day09


class Account:
     def __init__(self, account_number, owner, balance=0):
          self.account_number = account_number
          self.owner = owner
          self.balance = balance
          self.history = []

     def deposit(self, amount):
          self.balance += amount
          self.history.append(('deposit', amount))
          print(f"Deposited {amount}. Balance: {self.balance}")

     def withdraw(self, amount):
          if amount > self.balance:
               print("Not enough money")
               return
          self.balance -= amount
          self.history.append(('withdraw', amount))
          print(f"Took {amount}. Balance: {self.balance}")

     def undo_last(self):
          if not self.history:
               print("No transactions")
               return
          txn_type, amount = self.history.pop()
          if txn_type == 'deposit':
               self.balance -= amount
               print(f"Undid deposit of {amount}. Balance: {self.balance}")
          else:
               self.balance += amount
               print(f"Undid withdrawal of {amount}. Balance: {self.balance}")

class AccountRegistry:
     def __init__(self):
          self.by_number = {}
          self.order = []

     def add(self, account):
          self.by_number[account.account_number] = account
          self.order.append(account.account_number)
          print(f"Added account {account.account_number}")

     def find(self, number):
          return self.by_number.get(number)

     def list_all(self):
          return [self.by_number[num] for num in self.order]

     def top_by_balance(self, n=5):
          accts = sorted(self.by_number.values(), key=lambda a: a.balance, reverse=True)
          return accts[:n]

     def binary_search(self, sorted_list, target):
          low, high = 0, len(sorted_list) - 1
          while low <= high:
               mid = (low + high) // 2
               if sorted_list[mid] < target:
                    low = mid + 1
               elif sorted_list[mid] > target:
                    high = mid - 1
               else:
                    return mid
          return -1

     def find_by_number(self, number):
          nums = sorted(self.by_number.keys())
          i = self.binary_search(nums, number)
          if i == -1:
               return None
          return self.by_number[nums[i]]

     def total_transactions(self, number):
          account = self.find(number)
          if account is None:
               return 0
          return self._recursive_total(account.history, 0)

     def _recursive_total(self, history, index):
          if index >= len(history):
               return 0
          txn_type, amount = history[index]
          return amount + self._recursive_total(history, index + 1)


class Branch:
     def __init__(self, name):
          self.name = name
          self.accounts = []
          self.children = []

     def add_account(self, account):
          self.accounts.append(account)

     def add_child(self, branch):
          self.children.append(branch)

     def total_balance(self):
          total = sum(acc.balance for acc in self.accounts)
          for child in self.children:
               total += child.total_balance()
          return total


class Bank:
     def __init__(self):
          self.transfers = {}   

     def add_transfer(self, from_branch, to_branch):
          if from_branch not in self.transfers:
               self.transfers[from_branch] = []
          self.transfers[from_branch].append(to_branch)

     def bfs(self, start):
          visited = set()
          queue = [start]
          reachable = []

          while queue:
               branch = queue.pop(0)
               if branch not in visited:
                    visited.add(branch)
                    reachable.append(branch)
                    for neighbor in self.transfers.get(branch, []):
                         if neighbor not in visited:
                              queue.append(neighbor)
          return reachable



if __name__ == "__main__":
     registry = AccountRegistry()

     almaz = Account("1000001", "Almaz", 1000)
     bekele = Account("1000002", "Bekele", 500)
     chaltu = Account("1000003", "Chaltu", 2000)

     registry.add(almaz)
     registry.add(bekele)
     registry.add(chaltu)

     almaz.deposit(300)
     almaz.withdraw(50)
     bekele.deposit(1000)
     chaltu.withdraw(500)


     for acc in registry.list_all():
          print(f"  {acc.account_number} — {acc.owner} — {acc.balance}")

     print("\nTop accounts")
     for acc in registry.top_by_balance(2):
          print(f"  {acc.owner}: {acc.balance}")

     found = registry.find_by_number("1000001")
     if found:
          print(f"Found: {found.owner}, balance: {found.balance}")

     total = registry.total_transactions("1000001")
     print(f"Total transaction amount for Almaz: {total} ETB")
     print(f"History: {len(almaz.history)}")

     almaz.undo_last()
     almaz.undo_last()
     almaz.undo_last()

     head_office = Branch("Head Office")
     region1 = Branch("Region 1")
     branch1 = Branch("Branch 1")
     branch2 = Branch("Branch 2")

     head_office.add_child(region1)
     region1.add_child(branch1)
     region1.add_child(branch2)

     head_office.add_account(almaz)
     region1.add_account(bekele)
     branch1.add_account(chaltu)

     print(f"Total balance in the bank: {head_office.total_balance()} ETB")


     bank = Bank()
     bank.add_transfer("CBE-1", "CBE-2")
     bank.add_transfer("CBE-1", "CBE-3")
     bank.add_transfer("CBE-2", "CBE-4")
     bank.add_transfer("CBE-3", "CBE-5")
     bank.add_transfer("CBE-4", "CBE-2") 

     reachable = bank.bfs("CBE-1")
     print(f"Branches reachable from CBE-1: {reachable}")