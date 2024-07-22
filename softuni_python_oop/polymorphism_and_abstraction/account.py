from typing import Optional


class Account:
    def __init__(self, owner: str, amount: Optional[int] = 0):
        self.owner = owner
        self.amount = amount
        self._transactions = []

    def handle_transaction(self, transaction_amount):
        if self.amount < 0:
            raise ValueError("sorry cannot go in debt!")
        self.amount += transaction_amount
        self._transactions.append(transaction_amount)
        return f"New balance: {self.amount}"

    def add_transaction(self, amount):
        if isinstance(amount, int):
            self.handle_transaction(amount)
        else:
            raise ValueError("please use int for amount")

    @property
    def balance(self):
        return self.amount

    def __str__(self):
        return f"Account of {self.owner} with starting amount: {self.amount}"

    def __repr__(self):
        return f"Account({self.owner}, {self.amount})"

    def __len__(self):
        return len(self._transactions)

    def __getitem__(self, index):
        return self._transactions[index]

    def __reversed__(self):
        return reversed([t for t in self._transactions])

    def __ge__(self, other: 'Account'):
        return self.amount >= other.amount

    def __gt__(self, other: 'Account'):
        return self.amount > other.amount

    def __eq__(self, other: 'Account'):
        return self.amount == other.amount

    def __ne__(self, other: 'Account'):
        return self.amount != other.amount

    def __add__(self, other: 'Account'):
        third_account = Account(f"{self.owner}&{other.owner}", self.amount + other.amount)
        third_account._transactions.extend(self._transactions)
        third_account._transactions.extend(other._transactions)
        return third_account
