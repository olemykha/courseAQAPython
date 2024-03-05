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
import logging

TERMINAL_SEPARATOR = '-' * 42
_log = logging.getLogger('Logging')


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

    @staticmethod
    def generate_card_number():
        return random.randint(1000000000000001, 9999999999999999)

    @staticmethod
    def generate_pin():
        return random.randint(0000, 9999)

    @staticmethod
    def generate_cvv():
        return random.randint(000, 999)

    @staticmethod
    def calculate_end_date():
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
        _log.info('Closing account.')
        if self.__balance != 0:
            if to_card:
                to_card.top_up_balance(self.__balance)
                transferred_amount = self.__balance
                self.__balance = 0.00
                _log.info(f'The account closed successfully. '
                          f'Remaining balance transferred to '
                          f'{to_card.name} {to_card.surname}. '
                          f'Transferred amount: '
                          f'{transferred_amount} {self.currency}')
                return True
            else:
                _log.info("The account cannot be closed "
                          "as it has a positive balance. "
                          "Please provide an account to transfer funds.")
                return False
        else:
            self.__balance = 0.00
            _log.info("The account closed successfully")
            return True

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        self.__pin = value

    @property
    def cvv(self):
        return self.__cvv

    @cvv.setter
    def cvv(self, value):
        self.__cvv = value

    @property
    def end_date(self):
        return self.__expiration_date

    @end_date.setter
    def end_date(self, value):
        self.__expiration_date = value

    def __str__(self):
        card_number_str = str(self._card_number)
        return f"Card details: \n"\
               f"{' ' * 31}Cardholder - {self.name} {self.surname}\n" \
               f"{' ' * 31}Card Number - {'*' * 12}{card_number_str[-4:]}\n" \
               f"{' ' * 31}CVV - ***\n" \
               f"{' ' * 31}Expired date - {self.__expiration_date}\n" \
               f"{' ' * 31}Balance - {self.__balance} {self.currency}\n" \
               f"{' ' * 31}Card state - {'Blocked' if self._is_blocked else 'Active'}"


if __name__ == '__main__':
    log_formatter = (logging.Formatter
                     ('%(asctime)s [%(levelname)s] %(message)s'))
    console_handler = logging.StreamHandler()
    console_handler.setFormatter(log_formatter)
    _log.addHandler(console_handler)
    _log.setLevel(logging.INFO)

    card1 = (BankCard
             ("Oleksandr", "Mykha"))
    card2 = (BankCard
             ("Evgen", "Sivach"))
    card3 = (BankCard
             ("Iryna", "Mykha"))

    _log.info(BankCard.get_bank_info())
    _log.info(TERMINAL_SEPARATOR)  # Just for readability in the terminal.

    check_balance = card1.check_balance()
    _log.info(f'Current balance: '
              f'{card1.check_balance()} ' + BankCard.get_currency())
    _log.info(card1)
    _log.info(TERMINAL_SEPARATOR)

    top_up_balance = card1.top_up_balance(1000)  # Refill bank acc
    _log.info(f'Top-up successful. '
              f'Added: {top_up_balance} ' + BankCard.get_currency())
    _log.info(f'Current balance: '
              f'{card1.check_balance()} ' + BankCard.get_currency())
    _log.info(card1)
    _log.info(TERMINAL_SEPARATOR)

    top_down_balance = card1.top_down_balance(500)  # Withdrawing funds
    _log.info(f'Withdrawal successful. '
              f'Withdrawn: {top_down_balance} ' + BankCard.get_currency())
    _log.info(f'Current balance: '
              f'{card1.check_balance()} ' + BankCard.get_currency())
    _log.info(card1)
    _log.info(TERMINAL_SEPARATOR)

    card1.block_card()  # Card blocking
    _log.info('Card has been blocked successfully.')
    _log.info(card1)
    _log.info(TERMINAL_SEPARATOR)

    card1.unblock_card()  # Card unblocking
    _log.info('Card has been unblocked successfully.')
    _log.info(card1)
    _log.info(TERMINAL_SEPARATOR)

    transfer_money = card1.transfer_money(card2, 200)  # Money transferring
    _log.info(f'Money has been transferred successfully. '
              f'Transferred: {transfer_money} ' + BankCard.get_currency())
    _log.info(card1)
    _log.info("Transferred to ↓")
    _log.info(card2)
    _log.info(TERMINAL_SEPARATOR)

    _log.info(card1.close_account())  # Closing acc with positive balance
    _log.info(TERMINAL_SEPARATOR)
    _log.info(card1.close_account(card3))  # Closing acc provision another acc
