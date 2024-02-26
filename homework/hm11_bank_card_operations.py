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

TERMINAL_SEPARATOR = '-' * 42


class BankCard:
    bank_name = "StereoBank"
    currency = "USD"

    def __init__(self, name, surname, card_number, pin, cvv, end_date):
        self.__card_statement = 0.00
        self.__is_blocked = False
        self.__name = name
        self.__surname = surname
        self.__card_number = card_number
        self.__pin = pin
        self.__cvv = cvv
        self.__end_date = end_date

    @classmethod
    def get_bank_info(cls):
        return f'Bank: {cls.bank_name}, Currency: {cls.currency}'

    @classmethod
    def get_currency(cls):
        return cls.currency

    def open_account(self):
        self.__card_statement = 0.00

    def check_balance(self):
        return self.__card_statement

    @staticmethod
    def validate_card_number(card_number):
        if len(str(card_number)) != 16:
            return False
        return True

    def top_up_balance(self, amount):
        self.__card_statement = self.__card_statement + amount
        return amount

    def top_down_balance(self, amount):
        if self.__card_statement - amount < 0:
            raise (ValueError
                   ('There are not enough funds to perform this operation.'))
        self.__card_statement = self.__card_statement - amount
        return amount

    def transfer_money(self, to_card, amount):
        if self.__card_statement - amount < 0:
            raise (ValueError
                   ('There are not enough funds to perform this operation.'))
        self.__card_statement -= amount
        to_card.top_up_balance(amount)
        return amount

    def block_card(self):
        self.__is_blocked = True

    def unblock_card(self):
        self.__is_blocked = False

    def is_blocked(self):
        return self.__is_blocked

    def close_account(self, to_card=None):
        if self.__card_statement != 0:
            if to_card:
                to_card.top_up_balance(self.__card_statement)
                self.__card_statement = 0.00
                return (f'The account closed successfully. '
                        f'Remaining balance transferred to '
                        f'{to_card.__name} {to_card.__surname}.')
            else:
                return ("The account cannot be closed "
                        "as it has a positive balance. "
                        "Please provide account to transfer funds.")
        else:
            self.__card_statement = 0.00
            return "The account closed successfully."

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

    def get_card_statement(self):
        return self.__card_statement

    def get_card_number(self):
        return self.__card_number

    def get_pin(self):
        return self.__pin

    def set_pin(self, pin):
        self.__pin = pin

    def get_cvv(self):
        return self.__cvv

    def get_end_date(self):
        return self.__end_date

    def __str__(self):
        return f"Cardholder: {self.__name} {self.__surname}\n" \
               f"Card Number: {'*' * 12}{self.__card_number[-4:]}\n" \
               f"CVV: ***\n" \
               f"Expired date: {self.__end_date}\n" \
               f"Balance: {self.__card_statement} {self.currency}\n" \
               f"Card state: {'Blocked' if self.__is_blocked else 'Active'}"


if __name__ == '__main__':
    card1 = (BankCard
             ("Oleksandr", "Mykha",
              "1234567890123456", "1234", "123", "12/24"))
    card2 = (BankCard
             ("Evgen", "Sivach",
              "9876543210987654", "5678", "456", "12/25"))
    card3 = (BankCard
             ("Iryna", "Mykha",
              "9876543210987654", "5678", "456", "12/25"))

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
