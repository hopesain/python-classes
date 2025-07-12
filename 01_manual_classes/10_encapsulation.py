class BankAccount:
    bank_name = "National Bank of Malawi"

    def __init__(self, account_holder, initial_balance):
        self.account_holder = account_holder #Public
        self._account_type = "Savings" #Protected
        self.__balance = 0 #Private
        self.deposit(initial_balance)

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited {amount}. New balance: {self.__balance}")
        else:
            print("Invalid deposit amount.")
    
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrew {amount}. New balance: {self.__balance}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def get_balance(self):
        return self.__balance
    
    def set_balance(self, amount):
        print("Direct balance modification is not allowed. Use deposit or withdraw methods.")

    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def balance(self, amount):
        print("Direct balance modification is not allowed. Use deposit or withdraw methods.")


### TESTING IT ############
acc = BankAccount("Hope", 500)

print("\n🔍 Trying to access public attributes:")
print(acc.account_holder)      # ✅ Works
print(acc.bank_name)           # ✅ Works (class attribute)

print("\n⚠️ Trying to access protected attribute:")
print(acc._account_type)       # ⚠️ Works, but shouldn't be used directly

print("\n❌ Trying to access private attribute:")
# print(acc.__balance)         # ❌ AttributeError

print("\n✅ Accessing private via method:")
print("Balance (get_balance):", acc.get_balance())   # ✅ Works

print("\n✅ Accessing private via property:")
print("Balance (property):", acc.balance)            # ✅ Cleaner

print("\n🪙 Depositing and Withdrawing:")
acc.deposit(250)          # ✅ Adds 250
acc.withdraw(100)         # ✅ Removes 100
acc.withdraw(1000)        # ❌ Insufficient

print("\n⛔ Trying to set balance directly:")
acc.set_balance(10000)    # ❌ Not allowed

print("\n⛔ Trying to override balance using property:")
acc.balance = 999999      # ❌ Blocked in setter