import unittest
from app.entities.transaction import Transaction
from app.usecases.authorize_transaction import AuthorizeTransaction
from app.repositories.transaction_repository import BalanceRepository

class TestAuthorizeTransaction(unittest.TestCase):
    def setUp(self):
        self.repository = BalanceRepository()
        self.authorize_transaction = AuthorizeTransaction(self.repository)

    def test_transaction_approved(self):
        transaction = Transaction(account_id="123", amount=50, mcc="5411", merchant="PADARIA")
        result = self.authorize_transaction.execute(transaction)
        self.assertEqual(result["code"], "00")

    def test_insufficient_funds(self):
        transaction = Transaction(account_id="123", amount=300, mcc="5811", merchant="PADARIA")
        result = self.authorize_transaction.execute(transaction)
        self.assertEqual(result["code"], "51")

if __name__ == '__main__':
    unittest.main()
