import unittest

from oopAccount.account import Account
from oopAccount.exceptions.insufficient_funds_exception import InsufficientFundsException
from oopAccount.exceptions.invalid_amount_exception import InvalidAmountException
from oopAccount.exceptions.invalid_pin_exception import InvalidPinException


class TestAccount(unittest.TestCase):
    def setUp(self):
        self.account: Account = Account("John Doe", 1, "1234")

    def test_account_is_empty(self):
        self.assertEqual(0, self.account.check_balance("1234"))

    def test_deposit_10k(self):
        self.account.deposit(10_000)

        self.assertEqual(10_000, self.account.check_balance("1234"))

    def test_deposit_twice(self):
        self.account.deposit(10_000)
        self.account.deposit(10_000)

        self.assertEqual(20_000, self.account.check_balance("1234"))

    def test_deposit_non_positive_amount(self):
        with self.assertRaises(InvalidAmountException):
            self.account.deposit(0)
        with self.assertRaises(InvalidAmountException):
            self.account.deposit(-5000)

        self.assertEqual(0, self.account.check_balance("1234"))

    def test_deposit10k_withdraw7k_BalanceIs3k(self):
        self.account.deposit(10_000)
        self.account.withdraw(7000, "1234")

        self.assertEqual(3000, self.account.check_balance("1234"))

    def test_withdrawNonPositiveAmount_raisesInvalidAmountException(self):
        self.account.deposit(10_000)
        self.assertEqual(10_000, self.account.check_balance("1234"))

        with self.assertRaises(InvalidAmountException):
            self.account.withdraw(0, "1234")
        with self.assertRaises(InvalidAmountException):
            self.account.withdraw(-5000, "1234")

        self.assertEqual(10_000, self.account.check_balance("1234"))

    def test_withdraw_more_than_balance(self):
        self.account.deposit(10_000)
        self.assertEqual(10_000, self.account.check_balance("1234"))

        with self.assertRaises(InsufficientFundsException):
            self.account.withdraw(10_001, "1234")
        with self.assertRaises(InsufficientFundsException):
            self.account.withdraw(15_000, "1234")

        self.assertEqual(10_000, self.account.check_balance("1234"))

    def test_withdraw_using_incorrect_pin(self):
        self.account.deposit(10_000)
        self.assertEqual(10_000, self.account.check_balance("1234"))

        with self.assertRaises(InvalidPinException):
            self.account.withdraw(5_000, "0000")

        self.assertEqual(10_000, self.account.check_balance("1234"))

    def test_check_balance_using_incorrect_pin(self):
        with self.assertRaises(InvalidPinException):
            self.account.check_balance("4444")

    def test_check_balance_with_incorrect_pin_exception_message(self):
        with self.assertRaises(InvalidPinException) as e:
            self.account.check_balance("0000")

        self.assertEqual("PIN provided is not valid.", str(e.exception))

    def test_deposit_withdraw_with_incorrect_pin_test_insufficient_exception_message(self):
        self.account.deposit(2_000)
        self.assertEqual(2_000, self.account.check_balance("1234"))

        with self.assertRaises(InsufficientFundsException) as e:
            self.account.withdraw(5_000, "1234")
        self.assertEqual("Insufficient funds to perform this operation.", str(e.exception))

        self.assertEqual(2_000, self.account.check_balance("1234"))

    def test_deposit_negative_amount(self):
        self.assertEqual(0, self.account.check_balance("1234"))

        with self.assertRaises(InvalidAmountException) as e:
            self.account.deposit(-5_000)
        self.assertEqual("Amount must be greater than zero.", str(e.exception))

        self.assertEqual(0, self.account.check_balance("1234"))

    def test_customary_setter_getter(self):
        self.assertEqual("John Doe", self.account.get_name())
        self.assertEqual(1, self.account.get_number())
