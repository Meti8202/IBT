# A Branch tree (head office → regions → branches, each holding accounts) with a recursive total_balance(), and a transfers graph (account → accounts it has paid) with a bfs() that finds who is reachable. Your registry stores accounts; now model the relationships between them. Copy your day08/registry.py into day09/, then add a Branch tree with a recursive balance total and a transfers graph you can traverse with BFS. Push the result to your day09 folder before Day 10, the Module 1 review and assessment.
# Requirements
# Build a Branch class with children and accounts; nest at least three levels deep.
# Write a recursive total_balance() that sums a branch and all its sub-branches.
# Build a transfers graph as a dict of account number → list of recipients.
# Write bfs(transfers, start) returning every account reachable from a given one.

class BankConfig:
     _instance = None

     def __new__(cls):
          if cls._instance is None:
               cls._instance = super().__new__(cls)
          return cls._instance

     def __init__(self):
          if not hasattr(self, 'initialized'):
               self.interest_rate = 0.03
               self.overdraft_limit = 5000
               self.initialized = True

class Account:
     def __init__(self, owner, number, balance=0):
          self.owner = owner
          self.account_number = number
          self.__balance = balance
          self.observers = []
          self.history = []

     @property
     def balance(self):
          return self.__balance

     def deposit(self, amount):
          if amount <= 0:
               raise ValueError("Amount must be positive")
          self.__balance += amount
          self.history.append(('deposit', amount))
          self._notify("deposit", amount)

     def withdraw(self, amount):
          if amount > self.balance:
               raise ValueError("You don't have enough money!")
          self.__balance -= amount
          self.history.append(('withdraw', amount))
          self._notify("withdraw", amount)

     def undo_last(self):
          if not self.history:
               print("No transactions to undo.")
               return
          txn_type, amount = self.history.pop()
          if txn_type == 'deposit':
               self.__balance -= amount
               print(f"Undid deposit of {amount}. Balance: {self.balance}")
          else:
               self.__balance += amount
               print(f"Undid withdrawal of {amount}. Balance: {self.balance}")

     def statement(self):
          print(f"{self.owner} with account number {self.account_number} has {self.balance} ETB.")

     def subscribe(self, observer):
          self.observers.append(observer)

     def _notify(self, action, amount):
          for observer in self.observers:
               observer.notify(self, action, amount)

class SavingsAccount(Account):
     def __init__(self, owner, number, balance=0):
          super().__init__(owner, number, balance)
          self.rate = BankConfig().interest_rate

     def add_interest(self):
          self.deposit(self.balance * self.rate)

     def statement(self):
          print(f"[Savings] {self.owner} with account number {self.account_number} has {self.balance} ETB.")

class CurrentAccount(Account):
     def __init__(self, owner, number, balance=0):
          super().__init__(owner, number, balance)
          self.overdraft = BankConfig().overdraft_limit

     def withdraw(self, amount):
          new_balance = self.balance - amount
          if new_balance < -self.overdraft:
               raise ValueError("Reached overdraft limit")
          self._Account__balance = new_balance
          self.history.append(('withdraw', amount))
          self._notify("withdraw", amount)

     def statement(self):
          print(f"[Current] {self.owner} with account number {self.account_number} has {self.balance} ETB.")

class SMSAlert:
     def notify(self, account, action, amount):
          print(f"SMS Alert: {account.owner}, you have {action} of {amount} ETB.")

class AuditLog:
     def notify(self, account, action, amount):
          print(f"Audit Log: {account.owner} did a {action} of {amount} ETB. Balance: {account.balance} ETB.")

class AccountFactory:
     @staticmethod
     def create(kind, owner, number, balance=0):
          if kind == "savings":
               return SavingsAccount(owner, number, balance)
          elif kind == "current":
               return CurrentAccount(owner, number, balance)
          else:
               raise ValueError("unknown account type")

class AccountRegistry:
     def __init__(self):
          self.by_number = {}
          self.order = []

     def add(self, account):
          self.by_number[account.account_number] = account
          self.order.append(account.account_number)

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
          self.children = []      
          self.accounts = []      

     def add_account(self, account):
          self.accounts.append(account)

     def add_child(self, branch):
          self.children.append(branch)

     def total_balance(self):
          total = sum(acc.balance for acc in self.accounts)
          for child in self.children:
               total += child.total_balance()
          return total


def bfs(transfers, start):
     visited = set()
     queue = [start]
     visited.add(start)

     while queue:
          current = queue.pop(0)
          for neighbor in transfers.get(current, []):
               if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

     return visited


if __name__ == "__main__":
     registry = AccountRegistry()

     almaz = Account("Almaz", "569978645", 1000)
     dawit = AccountFactory.create("savings", "Dawit", "9876565756", 2000)
     hana = AccountFactory.create("current", "Hana", "1092546577", 3000)

     registry.add(almaz)
     registry.add(dawit)
     registry.add(hana)

     dawit.deposit(500)
     dawit.withdraw(200)
     dawit.withdraw(200)
     hana.deposit(150)

     for acc in registry.list_all():
          print(f"  {acc.account_number} – {acc.owner} – {acc.balance}")

     print("Top accounts:")
     for acc in registry.top_by_balance(2):
          print(f"  {acc.owner}: {acc.balance}")

     found = registry.find_by_number("9876565756")
     print(f"Found account for {found.owner} with balance {found.balance}")

     total_dawit = registry.total_transactions("9876565756")
     print(f"Total of Dawit's transactions (ETB): {total_dawit}")
     print(f"Dawit's history: {len(dawit.history)}")

     sms = SMSAlert()
     audit = AuditLog()
     dawit.subscribe(sms)
     dawit.subscribe(audit)
     hana.subscribe(sms)
     hana.subscribe(audit)

     dawit.add_interest()
     hana.withdraw(2500)
     dawit.undo_last()
     dawit.undo_last()

     head_office = Branch("Head Office")
     region1 = Branch("Region 1")
     region2 = Branch("Region 2")
     branch1 = Branch("Branch 1")
     branch2 = Branch("Branch 2")
     branch3 = Branch("Branch 3")

     head_office.add_child(region1)
     head_office.add_child(region2)

     region1.add_child(branch1)
     region1.add_child(branch2)
     region2.add_child(branch3)

     head_office.add_account(almaz)      
     region1.add_account(dawit)         
     branch1.add_account(hana)           

     print(f"Total balance of Head Office: {head_office.total_balance()} ETB")
     print(f"Total balance of Region 1: {region1.total_balance()} ETB")
     print(f"Total balance of Branch 1: {branch1.total_balance()} ETB")

     transfers = {
          "569978645": ["9876565756"],           # Almaz paid Dawit
          "9876565756": ["1092546577", "569978645"],  # Dawit paid Hana and Almaz
          "1092546577": ["9876565756"],          # Hana paid Dawit
     }

     start_account = "569978645"  # Almaz's account
     reachable = bfs(transfers, start_account)

     print(f"\nAccounts reachable from {start_account} (Almaz):")
     for acc_number in sorted(reachable):
          account = registry.find(acc_number)
          if account:
               print(f"  {acc_number} – {account.owner}")
          else:
               print(f"  {acc_number} – (not in registry)")