# Three additions to the AccountRegistry: a top_by_balance(n) leaderboard, a find_by_number(number) that uses binary search over sorted account numbers, and a recursive total_transactions(number). Your registry holds many accounts; now make them rankable and searchable. Copy your day07/registry.py into day08/, then add a balance leaderboard, a binary search by account number, and a recursive transaction total. Push the result to your day08 folder before Day 9, where you'll model hierarchical and connected data with trees and graphs.
# Requirements
# Add top_by_balance(n) using sorted(key=lambda a: a.balance, reverse=True); return the top n.
# Write your own binary_search and use it in find_by_number(number) over the sorted account numbers.
# Add a recursive total_transactions(number) that sums one account's transaction history.
# Do not use the in operator or a loop for the number search — the point is to practise binary search.

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

     print("\nTop accounts:")
     for acc in registry.top_by_balance(2):
          print(f"  {acc.owner}: {acc.balance}")
          
     found = registry.find_by_number("9876565756")  # maybe i need to make this user input or sth like that
     print(f"\nFound account for {found.owner} with balance {found.balance}")

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