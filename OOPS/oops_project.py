from encapsulation import *


Rahul = Account("Rahul", 1000)

Shristhi = Account("Shristhi", 2000)

Rahul.show_balance()
Shristhi.show_balance()

Rahul.deposit(500)
Shristhi.deposit(1000)

Rahul.withdraw(200)
Shristhi.withdraw(300)

Rahul.transfer(100, Shristhi)

Jim = InterestRewardAcc("Jim", 1000)

Jim.show_balance()

Jim.deposit(100)

Jim.transfer(100, Rahul)

Lodu = SavingAcc("Lodu", 1000)

Lodu.show_balance()

Lodu.withdraw(100)
