<<<<<<< HEAD
class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, account):
        self.balance += account

    def printAccount(self):
        if self.balance >= 0:
           return True
        else:
           return False

s = Bank(input(), int(input()))
while(1):
    n = int(input())
    if n == 0:
        break
    else:
        s.deposit(n)
print(s.printAccount())
=======
class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, account):
        self.balance += account

    def printAccount(self):
        if self.balance >= 0:
           return True
        else:
           return False

s = Bank(input(), int(input()))
while(1):
    n = int(input())
    if n == 0:
        break
    else:
        s.deposit(n)
print(s.printAccount())
>>>>>>> 68ee922863d7bbad933d1b77aaeeaf5cf621a9da
