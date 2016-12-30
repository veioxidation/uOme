from utils import Money


class User:
    def __init__(self, name, id_number=0):
        self.ID = id_number
        self.name = name
        self.RB = 0
        self.TB = 0

    def AddToRB(self, amount):
        self.RB += amount

    def AddToTB(self, amount):
        self.TB += amount

    def UserInfo(self):
        user_info = "Name: {}\n" \
                    "Real balance: {}\n" \
                    "Theoritical balance: {}\n" \
                    "BALANCE: {}".format(self.name,
                                         Money(self.RB),
                                         Money(self.TB),
                                         Money(self.Balance()))
        print(user_info)

    def Balance(self):
        return round(self.RB - self.TB, 2)
