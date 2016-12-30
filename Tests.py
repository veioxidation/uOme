from Group import Group
from User import User
from utils import Money

new_group = Group(User("Przemek"))

for name in ['Ania', 'Tola', "Marian", 'Kamila']:
    new_group.CreateUser(name)

new_group.AddEntry("Jedzenie", 10000, 0, [1, 2, 3])
new_group.AddEntry("hehehe", 10000, 2, [1, 2, 3, 4])
new_group.AddEntry("hehehehe", 1000, 2, 'me')
new_group.AddEntry("eeeeeeeee", 10000, 3, 'all')
new_group.AddEntry("makarenba", 10000, 1, [1, 2, 1])

new_group.ExportAll()



new_group.GroupInfo()

second_group = Group()
second_group.ImportAll()


print('Summaric money: {}'.format(Money(second_group.SumMoney())), "\n")

second_group.SolveBalance()