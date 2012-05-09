import requests
import simplejson
from gateway_transaction import GatewayTransaction

class GatewayRequest(object):
    def __init__(self, endpoint, action='/'):
        self.endpoint = endpoint
        self.action = action

    def request_uri(self):
        return self.endpoint + self.action

    def post(self, params):
        headers = { 'content-type': 'application/json' }
        data = simplejson.dumps(params)
        return requests.post(self.request_uri(), data=data, headers=headers)

    def get(self, params):
        return requests.get(self.request_uri(), params=params)

class GatewayResponse(object):
    def __init__(self, response):
        self.response_object = response
        self.status_code = response.status_code
        self.headers = response.headers
        self.raw_body = response.text
        self.body = simplejson.loads(response.text)

    def content_type(self):
        return self.headers.get('content-type')

    def parse(self):
        gateway_transaction = GatewayTransaction()
        transaction_node = self.body.get('transacao') or {}
        error_node = transaction_node.get('erro') or {}
        gateway_transaction.id = transaction_node.get('id')
        gateway_transaction.status = transaction_node.get('status')
        gateway_transaction.url_acesso = transaction_node.get('url_acesso')
        gateway_transaction.meio_pagamento = transaction_node.get('meio_pagamento')
        gateway_transaction.numero_pedido = transaction_node.get('numero_pedido')
        gateway_transaction.detalhes = transaction_node.get('detalhes')
        gateway_transaction.erro = error_node
        gateway_transaction.erro_codigo = error_node.get('codigo')
        gateway_transaction.erro_mensagem = error_node.get('mensagem')
        return gateway_transaction
