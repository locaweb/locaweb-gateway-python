# Locaweb-Gateway-Python

## Instalação

Pip:

    pip install locaweb_gateway

Easy Install:

    easy_install locaweb_gateway

## Environment e token

O Gateway da Locaweb possui a sua forma de autenticação e dois ambientes para processamento das transações: o ambiente de produção e o ambiente de testes(sandbox).
Para se autenticar e passar o ambiente:

```python
   from locaweb_gateway import LocawebGatewayConfig
   LocawebGatewayConfig.environment = 'sandbox'
   LocawebGatewayConfig.token = '3a5bbed0-50d4-012f-8d73-0026bb5a6240'
```

## Criar Transação

```python
from locaweb_gateway import LocawebGateway

LocawebGatewayConfig.environment = 'sandbox'
LocawebGatewayConfig.token = '3a5bbed0-50d4-012f-8d73-0026bb5a6240'

transacao = LocawebGateway.criar({
   "url_retorno": 'http://foo.com/sucesso_pedido.php?pedido=12345',
   "capturar": True,
   "pedido": {
     "numero": "123",
     "total": "100.00",
     "moeda":  "real",
     "descricao": "Carrinho de Compras"
   },
   "pagamento": {
     "meio_pagamento": "boleto_itau",
     "bandeira": "visa",
     "cartao_numero": "4012001037141112",
     "cartao_cvv": "973",
     "parcelas": "1",
     "tipo_operacao": "credito_a_vista",
     "cartao_validade": "082015"
   },
   "comprador": {
     "nome": "Bruna da Silva",
     "documento": "12345678900",
     "endereco": "Rua da Casa",
     "numero": "23",
     "cep": "09710240",
     "bairro": "Centro",
     "cidade": u"São Paulo",
     "estado": "SP"
   }
})
```

## Consultar Transação

Imagine que você quer consultar a transação criada acima, basta fazer isso:

```python
  LocawebGateway.consultar(transacao.id)
```

# Capturar Transação

Se você passou a flag de "capturar" como false no exemplo acima, você precisará capturar em algum momento. Para isso, basta fazer:

```python
LocawebGateway.capturar(transacao.id)
```

# Cancelar Transação

Caso queira estornar/cancelar a transação criada acima, basta fazer:

```python
LocawebGateway.cancelar(transacao.id)
```

## Documentação

[Documentação do Gateway de Pagamentos Locaweb](http://docs.gatewaylocaweb.com.br)