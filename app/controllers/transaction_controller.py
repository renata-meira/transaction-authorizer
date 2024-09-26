from flask import Flask, request, jsonify
from app.usecases.authorize_transaction import AuthorizeTransaction
from app.repositories.transaction_repository import BalanceRepository

app = Flask(__name__)

@app.route('/transaction', methods=['POST'])
def authorize():
    data = request.get_json()
    transaction = Transaction(
        account_id=data['account'],
        amount=data['totalAmount'],
        mcc=data['mcc'],
        merchant=data['merchant']
    )

    usecase = AuthorizeTransaction(BalanceRepository())
    result = usecase.execute(transaction)

    return jsonify(result), 200
