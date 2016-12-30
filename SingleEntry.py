import datetime


class SingleEntry:
    def __init__(self, name, amount, payer, paid_for):
        self.name = ""
        self.amount = amount
        self.payer = payer
        self.paid_for = paid_for
        self.time = datetime.datetime.now().isoformat()

    def EditEntry(self, **kwargs):
        for kwarg in kwargs:
            if kwarg in ['name', 'amount', 'payer']:
                if kwarg == 'name':
                    self.name = kwarg
                elif kwarg == 'amount':
                    self.amount = kwarg
                else:
                    self.payer = kwarg
