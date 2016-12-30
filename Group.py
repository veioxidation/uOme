from User import User
from SingleEntry import SingleEntry
from EntryRegistry import EntryRegistry
from Solver import SolveEntry
import xml.etree.ElementTree as ET
from utils import Money
import json


class Group:
    def __init__(self, owner=User('default'), filename='GOURP.json'):
        self.users = {owner.ID: owner}
        self.registry = EntryRegistry()
        self.UsersPath = ""
        self.JSONFilename = filename

    def CreateUser(self, username):
        _id = len(self.users)
        while _id in self.users:
            _id += 1
        self.users[_id] = User(username, _id)

    def DeleteUser(self, user_id):
        self.users.pop(user_id)

    def GetUserByID(self, id_num):
        return self.users[id_num]

    def ExportAll(self):

        file = open(self.JSONFilename, 'w+')
        user_list = []
        for u_id, u_class in self.users.items():
            user_list.append(u_class.__dict__)
        entry_list = []
        for entry in self.registry.entries:
            entry_list.append(entry.__dict__)
        json.dump([user_list, entry_list], file)

    def ImportRegistry(self):
        file = open(self.file, 'r+')
        self.entries = []

    def ImportAll(self):
        file = open(self.JSONFilename, 'r+')
        self.users = {}
        ld = json.load(file)
        users_dicts_list = ld[0]
        for users_dict in users_dicts_list:
            new_user = User("def")
            new_user.__dict__ = users_dict

            self.users[new_user.ID] = new_user

        entry_dicts_list = ld[1]
        for entry_dict in entry_dicts_list:
            new_entry = SingleEntry("", 0, 0, [0])
            new_entry.__dict__ = entry_dict
            self.registry.entries.append(new_entry)

    def AddEntry(self, name, amount, payer, paid_for):
        if isinstance(paid_for, str):
            pf_ids = {
                'all': [user for user in self.users],
                'me': [payer],
                'all_but_me': [user for user in self.users if user != payer]
            }
            paid_for_list = pf_ids[paid_for]
        else:
            paid_for_list = paid_for

        new_entry = SingleEntry(name, amount, payer, paid_for_list)
        self.registry.entries.append(new_entry)
        print("Entry: {} , amount: {} $ , paid by: {} for {}. Timestamp: {}".format(name, amount, payer, paid_for_list,
                                                                                    new_entry.time))
        SolveEntry(self, new_entry)
        self.registry.AddEntry(new_entry)

    def GroupInfo(self):
        for user in self.users.values():
            print('-' * 20, user.ID, '-' * 20)
            user.UserInfo()

    def SumMoney(self):
        return sum([user.RB for user in self.users.values()])

    def SolveBalance(self):
        _tolerance = 0.01
        balance_list = {user.ID: user.Balance() for user in self.users.values() if abs(user.Balance()) >= _tolerance}

        while 1:
            # find users with lowest and highest balances
            lowest_bal = 0
            highest_bal = 0
            lowest_id = None
            highest_id = None
            for i in balance_list:
                if lowest_bal > balance_list[i] or lowest_id == None:
                    lowest_bal = balance_list[i]
                    lowest_id = i
                if highest_bal < balance_list[i] or highest_id == None:
                    highest_bal = balance_list[i]
                    highest_id = i
            # transfer minimum of absolute of balances
            transfer_amount = min(abs(lowest_bal), highest_bal)
            balance_list[highest_id] -= transfer_amount
            balance_list[lowest_id] += transfer_amount
            print("{0} should be transferred from user {1} to user {2}.".format(Money(transfer_amount, space=10),
                                                                                self.users[lowest_id].name,
                                                                                self.users[highest_id].name))

            # remove user from dictionary if balance is equal to zero
            for user_id in [highest_id, lowest_id]:
                if abs(balance_list[user_id]) < _tolerance:
                    balance_list.pop(user_id)

            if len(balance_list) <= 1:
                break

        print("Transferring finished.")
