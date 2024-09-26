class AuthorizeTransaction:
    def __init__(self, balance_repository):
        self.balance_repository = balance_repository

    def execute(self, transaction):
        # Mapeia a transação para uma categoria de saldo
        category = transaction.map_mcc_to_category(transaction.mcc)

        # Verifica saldo da categoria mapeada
        balance = self.balance_repository.get_balance(transaction.account_id, category)
        if balance >= transaction.amount:
            self.balance_repository.decrease_balance(transaction.account_id, category, transaction.amount)
            return {"code": "00"}  # Transação aprovada
        else:
            # Verifica saldo de CASH como fallback
            cash_balance = self.balance_repository.get_balance(transaction.account_id, "CASH")
            if cash_balance >= transaction.amount:
                self.balance_repository.decrease_balance(transaction.account_id, "CASH", transaction.amount)
                return {"code": "00"}  # Transação aprovada com fallback
            else:
                return {"code": "51"}  # Saldo insuficiente
