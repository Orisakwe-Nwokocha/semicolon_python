import unittest

from oopAccount.account import Account
from oopAccount.bank import Bank


class TestBank(unittest.TestCase):
    def setUp(self):
        self.firstBank: Bank = Bank("First Bank")

    def test_register_customer(self):
        account: Account = self.firstBank.register_customer("John", "Doe", "1234")

        self.assertEqual(1, account.get_number())
        self.assertEqual("John Doe", account.get_name())

    def test_registerCustomer_findRegisteredAccount(self):
        account: Account = self.firstBank.register_customer("John", "Doe", "1234")
        expected = self.firstBank.find_account(1)

        self.assertEqual(expected, account)

    def test_findDifferentAccounts_accountsAreNotEqual(self):
        account1: Account = self.firstBank.register_customer("John", "Doe", "1234")
        account2: Account = self.firstBank.register_customer("John", "Doe", "1234")

        expected = self.firstBank.find_account(account2.get_number())
        self.assertNotEqual(expected, account1)
        self.assertNotEqual(account1.get_number(), account2.get_number())

    def test_account_is_empty(self):
        account: Account = self.firstBank.register_customer("John", "Doe", "1234")

        self.assertEqual(0, self.firstBank.check_balance(account.get_number(), "1234"))

    def test_deposit10k_balanceIs10k(self):
        account: Account = self.firstBank.register_customer("John", "Doe", "1234")
        self.firstBank.deposit(account.get_number(), 10_000)

        self.assertEqual(10_000, self.firstBank.check_balance(account.get_number(), "1234"))

    def test_deposit7k_withdraw2k_balanceIs5k(self):
        account: Account = self.firstBank.register_customer("John", "Doe", "1234")
        self.firstBank.deposit(account.get_number(), 7000)
        self.firstBank.withdraw(account.get_number(), 2000, "1234")

        self.assertEqual(5000, self.firstBank.check_balance(account.get_number(), "1234"))

    def test_deposit75kAnd5k_transfer25k_balanceIs30kAnd50k(self):
        john: Account = self.firstBank.register_customer("John", "Doe", "1234")
        jane: Account = self.firstBank.register_customer("Jane", "Doe", "0000")
        self.firstBank.deposit(john.get_number(), 75_000)
        self.firstBank.deposit(jane.get_number(), 5000)

        self.firstBank.transfer(john.get_number(), jane.get_number(), 25_000, "1234")

        self.assertEqual(30_000, self.firstBank.check_balance(jane.get_number(), "0000"))
        self.assertEqual(50_000, self.firstBank.check_balance(john.get_number(), "1234"))

    def test_removeAccount_findRemovedAccount_raisesValueErrorException(self):
        account = self.firstBank.register_customer("John", "Doe", "1234")
        self.assertIsNotNone(self.firstBank.find_account(account.get_number()))

        self.firstBank.remove_account(account.get_number(), "1234")
        with self.assertRaises(ValueError):
            self.firstBank.find_account(account.get_number())
