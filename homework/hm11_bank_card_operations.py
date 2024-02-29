"""
HOMEWORK11. Bank card operations.

Task Description:
-----------------
HOMEWORK11 involves the following task.
-Write class for bank card.
-Class should reflect card lifecycle, card operations etc.
-Use CVV, PIN, Name, Surname , end date, card_num as initial params.
-Class should have in addition to common logic some class attributes,
as minimum one class method and as minimum one staticmethod,
two or more getters/setters, __str_ magic method.
-Do not forget about block ""if __name__ == '__main__':""
and code there to check your class written logic.
"""
from datetime import datetime
import random

TERMINAL_SEPARATOR = '-' * 42


class BankCard:
    bank_name = "StereoBank"
    currency = "USD"

    def __init__(self, name, surname):
        self.__balance = 0.00
        self._is_blocked = False
        self.name = name
        self.surname = surname
        self._card_number = self.generate_card_number()
        self.__pin = self.generate_pin()
        self.__cvv = self.generate_cvv()
        self.__expiration_date = self.calculate_end_date()

    @classmethod
    def generate_card_number(cls):
        return random.randint(1000000000000001, 9999999999999999)

    @classmethod
    def generate_pin(cls):
        return random.randint(0000, 9999)

    @classmethod
    def generate_cvv(cls):
        return random.randint(000, 999)

    @classmethod
    def calculate_end_date(cls):
        current_date = datetime.now()
        end_year = current_date.year + 5
        end_month = current_date.month
        return f'{end_month:02d}/{end_year}'

    @classmethod
    def get_bank_info(cls):
        return f'Bank: {cls.bank_name}, Currency: {cls.currency}'

    @classmethod
    def get_currency(cls):
        return cls.currency

    @classmethod
    def _check_operation_allowed(cls, balance, amount):
        if balance - amount < 0:
            raise (ValueError
                   ('There are not enough funds to perform this operation.'))

    def open_account(self):
        self.__balance = 0.00

    def check_balance(self):
        return self.__balance

    def top_up_balance(self, amount):
        self.__balance = self.__balance + amount
        return amount

    def top_down_balance(self, amount):
        self._check_operation_allowed(self.__balance, amount)
        self.__balance -= amount
        return amount

    def transfer_money(self, to_card, amount):
        self._check_operation_allowed(self.__balance, amount)
        self.__balance -= amount
        to_card.top_up_balance(amount)
        return amount

    def block_card(self):
        self._is_blocked = True

    def unblock_card(self):
        self._is_blocked = False

    def is_blocked(self):
        return self._is_blocked

    def close_account(self, to_card=None):
        if self.__balance != 0:
            if to_card:
                to_card.top_up_balance(self.__balance)
                self.__balance = 0.00
                return (f'The account closed successfully. '
                        f'Remaining balance transferred to '
                        f'{to_card.name} {to_card.surname}.')
            else:
                return ("The account cannot be closed "
                        "as it has a positive balance. "
                        "Please provide account to transfer funds.")
        else:
            self.__balance = 0.00
            return "The account closed successfully."

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_surname(self):
        return self.surname

    def set_surname(self, surname):
        self.surname = surname

    def get_card_number(self):
        return self._card_number

    def get_pin(self):
        return self.__pin

    def get_cvv(self):
        return self.__cvv

    def get_end_date(self):
        return self.__expiration_date

    def __str__(self):
        card_number_str = str(self._card_number)
        return f"Cardholder: {self.name} {self.surname}\n" \
               f"Card Number: {'*' * 12}{card_number_str[-4:]}\n" \
               f"CVV: ***\n" \
               f"Expired date: {self.__expiration_date}\n" \
               f"Balance: {self.__balance} {self.currency}\n" \
               f"Card state: {'Blocked' if self._is_blocked else 'Active'}"


if __name__ == '__main__':

    card1 = (BankCard
             ("Oleksandr", "Mykha"))
    card2 = (BankCard
             ("Evgen", "Sivach"))
    card3 = (BankCard
             ("Iryna", "Mykha"))

print(BankCard.get_bank_info())
print(TERMINAL_SEPARATOR)  # Just for readability in the terminal.

check_balance = card1.check_balance()
print(f'Current balance: {card1.check_balance()} ' + BankCard.get_currency())
print(TERMINAL_SEPARATOR)

top_up_balance = card1.top_up_balance(1000)  # Refill bank account
print(f'Top-up successful. Added: {top_up_balance} ' + BankCard.get_currency())
print(f'Current balance: {card1.check_balance()} ' + BankCard.get_currency())
print(TERMINAL_SEPARATOR)

top_down_balance = card1.top_down_balance(500)  # Withdrawing funds
print(f'Withdrawal successful. '
      f'Withdrawn: {top_down_balance} ' + BankCard.get_currency())
print(f'Current balance: {card1.check_balance()} ' + BankCard.get_currency())
print(TERMINAL_SEPARATOR)

card1.block_card()  # Card blocking
print('Card has been blocked successfully.')
print(card1)
print(TERMINAL_SEPARATOR)

card1.unblock_card()  # Card unblocking
print('Card has been unblocked successfully.')
print(card1)
print(TERMINAL_SEPARATOR)

transfer_money = card1.transfer_money(card2, 200)  # Money transferring
print(f'Money has been transferred successfully. '
      f'Transferred: {transfer_money} ' + BankCard.get_currency())
print(card1)
print("Transferred to: ")
print(card2)
print(TERMINAL_SEPARATOR)

print(card1.close_account())  # Attempt to close card with positive balance
print(TERMINAL_SEPARATOR)
print(card1.close_account(card3))  # Attempt to close card with remaining bal
