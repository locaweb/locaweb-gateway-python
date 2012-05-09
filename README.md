# Locaweb-Gateway-Python

## Uso

    from locaweb_gateway import LocawebGateway, LocawebGatewayConfig
    import locaweb_gateway
    
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
         "cidade": "São Paulo",
         "estado": "SP"
       }
    })
    t = LocawebGateway.consultar(transacao.id)
    LocawebGateway.cancelar(transacao.id)
    LocawebGateway.capturar(transacao.id)

## Documentação

[Documentação do Gateway de Pagamentos Locaweb](http://docs.gatewaylocaweb.com.br)
