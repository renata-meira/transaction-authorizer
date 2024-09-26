from enum import Enum

class TransactionCategory(Enum):
    FOOD = "FOOD"
    MEAL = "MEAL"
    CASH = "CASH"

class Transaction:
    def __init__(self, account_id: str, amount: float, mcc: str, merchant: str):
        self.account_id = account_id
        self.amount = amount
        self.mcc = mcc
        self.merchant = merchant

    @staticmethod
    def map_mcc_to_category(mcc: str):
        if mcc in ["5411", "5412"]:
            return TransactionCategory.FOOD
        elif mcc in ["5811", "5812"]:
            return TransactionCategory.MEAL
        else:
            return TransactionCategory.CASH
