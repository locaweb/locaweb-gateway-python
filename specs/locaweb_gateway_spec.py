#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyvows import Vows, expect
from locaweb_gateway import LocawebGateway
import locaweb_gateway

locaweb_gateway.environment = 'unknown'

def create_params(payment_service):
    params = {
      "token": "3a5bbed0-50d4-012f-8d73-0026bb5a6240",
      "transacao": {
        "url_retorno": 'http://mystore.com/return',
        "pedido": {
          "numero":"654",
          "total":"100.00",
          "moeda":"real",
          "descricao":"My Camaro car!"
        },
        "pagamento":{
            "bandeira":"visa",
            "meio_pagamento": payment_service,
            "cartao_numero":"4012001037141112",
            "cartao_cvv":"973",
            "parcelas":"1",
            "tipo_operacao":"credito_a_vista",
            "cartao_validade":"082015"
        },
        "comprador":{
          "nome": "Bruna da Silva"
        }
      }
    }
    return params

