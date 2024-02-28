from oopBank.exceptions.insufficient_funds_exception import InsufficientFundsException
from oopBank.exceptions.invalid_amount_exception import InvalidAmountException
from oopBank.exceptions.invalid_pin_exception import InvalidPinException


class Account:
    def __init__(self, name: str, number: int, pin: str):
        self.validate_pin_format_and_length(pin)

        self.__name = name
        self.__balance = 0
        self.__number = number
        self.__pin = pin

    @staticmethod
    def validate_pin_format_and_length(pin: str):
        Account._validate_pin_format(pin)
        Account._validate_pin_length(pin)

    @staticmethod
    def _validate_pin_format(pin: str):
        digits = pin.isdigit()
        if not digits:
            raise InvalidPinException("PIN must consist of only digit numbers.")

    @staticmethod
    def _validate_pin_length(pin: str):
        valid = len(pin) == 4
        if not valid:
            raise InvalidPinException("PIN length must be four digits long.")

    def deposit(self, amount: int):
        self._validate_amount(amount)

        self.__balance += amount

    def withdraw(self, amount: int, pin: str):
        self._validate_withdraw_operation(amount, pin)

        self.__balance -= amount

    def check_balance(self, pin: str) -> int:
        self._validate_pin(pin)

        return self.__balance

    def _validate_withdraw_operation(self, amount, pin):
        self._validate_pin(pin)
        self._validate_amount(amount)
        self._ensure_sufficient_funds(amount)

    def _validate_pin(self, pin: str):
        if self.is_incorrect(pin):
            raise InvalidPinException("PIN provided is not valid.")

    def _ensure_sufficient_funds(self, amount: int):
        if amount > self.__balance:
            raise InsufficientFundsException("Insufficient funds to perform this operation.")

    @staticmethod
    def _validate_amount(amount: int):
        if amount <= 0:
            raise InvalidAmountException("Amount must be greater than zero.")

    def get_number(self):
        return self.__number

    def is_incorrect(self, pin: str):
        return self.__pin != pin

    def get_name(self):
        return self.__name
