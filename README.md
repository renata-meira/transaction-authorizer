# Transaction Authorizer

## Descrição

O **Transaction Authorizer** é uma aplicação Flask que permite a autorização de transações financeiras. A aplicação fornece uma API para processar transações, validando informações como ID da conta, valor da transação, código da categoria (MCC) e comerciante.

## Estrutura do Projeto

transaction-authorizer/ │ ├── app/ │ ├── init.py │ ├── controllers/ │ ├── entities/ │ ├── repositories/ │ └── usecases/ │ ├── tests/ │ ├── test_authorization.py │ ├── main.py ├── README.md └── requirements.txt

## Requisitos

- Python 3.12 ou superior
- Flask


## Instale as dependências

pip install -r requirements.txt

## Testes unitários

python -m unittest discover -s tests