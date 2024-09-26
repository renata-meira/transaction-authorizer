class BalanceRepository:
    def __init__(self):
        self.balances = {
            "123": {"FOOD": 100.0, "MEAL": 50.0, "CASH": 200.0}
        }

    def get_balance(self, account_id, category):
        return self.balances.get(account_id, {}).get(category, 0)

    def decrease_balance(self, account_id, category, amount):
        if account_id in self.balances and category in self.balances[account_id]:
            self.balances[account_id][category] -= amount
