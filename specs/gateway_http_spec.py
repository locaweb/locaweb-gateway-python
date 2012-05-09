#!/usr/bin/env python
# -*- coding: utf-8 -*-

from pyvows import Vows, expect
from locaweb_gateway.gateway_http import GatewayRequest, GatewayResponse

@Vows.batch
class GatewayRequestSpec(Vows.Context):
    class GatewayRequestURL(Vows.Context):
        def topic(self):
            return "http://foobar.com"

        def should_join_the_base_endpoint_with_root_action(self, topic):
            gateway_request = GatewayRequest(topic, action='/')
            expect(gateway_request.request_uri()).to_equal('http://foobar.com/')

        def should_join_the_base_endpoint_with_other_action(self, topic):
            gateway_request = GatewayRequest(topic, action='/v1/transacao')
            expect(gateway_request.request_uri()).to_equal('http://foobar.com/v1/transacao')

class ResponseFixture(object):
    def __init__(self, headers={'content-type': 'application/json'}, body='{"transacao":{"erro":{"codigo":"001","mensagem":"Credenciais Inválidas"}}}'):
        self.status_code = 201
        self.headers = headers
        self.text = body

@Vows.batch
class GatewayResponseSpec(Vows.Context):
    class StoreTheResponseObject(Vows.Context):
        def topic(self):
            return ResponseFixture()

        def should_store_the_response_object(self, topic):
            expect(GatewayResponse(topic).response_object).to_equal(topic)

    class DefaultContentType(Vows.Context):
        def topic(self):
            return GatewayResponse(ResponseFixture())

        def should_return_the_content_type_as_json(self, topic):
            expect(topic.headers).to_equal({'content-type': 'application/json'})
            expect(topic.content_type()).to_equal("application/json")

    class EmptyContentType(Vows.Context):
        def topic(self):
            return GatewayResponse(ResponseFixture(headers={}))

        def should_return_a_none_content_type(self, topic):
            topic.content_type()
            expect(topic.content_type()).to_equal(None)

    class ParsingTheJSONToBodyAtrribute(Vows.Context):
        def topic(self):
            return GatewayResponse(ResponseFixture())

        def should_return_the_body_parsed(self, topic):
            expect(topic.body).to_be_instance_of(dict)
            expect(topic.body).to_equal({'transacao': {'erro': {'codigo': '001', 'mensagem': u'Credenciais Inválidas'}}})

        def should_have_a_raw_body(self, topic):
            expect(topic.raw_body).to_equal(ResponseFixture().text)

    class ParsingTheResponseToTransaction(Vows.Context):
        class WithGatewayResponseError(Vows.Context):
            def topic(self):
                return GatewayResponse(ResponseFixture()).parse()

            def should_parse_the_error_node(self, topic):
                expect(topic.erro).to_equal({'codigo': '001', 'mensagem': u'Credenciais Inválidas'})

            def should_parse_the_error_code(self, topic):
                expect(topic.erro_codigo).to_equal('001')

            def should_parse_the_error_node(self, topic):
                expect(topic.erro_mensagem).to_equal(u'Credenciais Inválidas')

        class WithGatewayBoletoResponse(Vows.Context):
            def topic(self):
                response_fixture = ResponseFixture(body='{"transacao": {"status": "aguardando pagamento", "url_acesso": "https://api.gplw.com.br/v1/boleto/uuid", "id": 158, "meio_pagamento": "boleto_itau", "numero_pedido": "852" }}')
                return GatewayResponse(response_fixture).parse()

            def should_parse_the_transaction_status(self, topic):
                expect(topic.status).to_equal("aguardando pagamento")

            def should_parse_the_transaction_id(self, topic):
                expect(topic.id).to_equal(158)

            def should_parse_the_transaction_url_acesso(self, topic):
                expect(topic.url_acesso).to_equal("https://api.gplw.com.br/v1/boleto/uuid")

            def should_parse_the_transaction_meio_pagamento(self, topic):
                expect(topic.meio_pagamento).to_equal('boleto_itau')

            def should_parse_the_transaction_numero_pedido(self, topic):
                expect(topic.numero_pedido).to_equal('852')

        class WithGatewayItauShoplineResponse(Vows.Context):
            def topic(self):
                response_fixture = ResponseFixture(body='{"transacao":{"id":154,"status":"aguardando pagamento","meio_pagamento":"itau_shopline","numero_pedido":654,"url_acesso":"https://api-gateway.devintegration.locaweb.com.br/v1/itau_shopline/3bc09d9e-e3be-4aec-bab4-5b2a94c06cbf","detalhes":{"nsu": "87643","tipo_pagamento": "visanet","data_pagamento":null,"numero_autorizacao": "908070","tipo_cartao":null},"erro":null}}')
                return GatewayResponse(response_fixture).parse()

            def should_parse_the_transaction_detalhes(self, topic):
                expect(topic.detalhes).to_equal({"nsu": "87643", "tipo_pagamento": "visanet", "data_pagamento": None, "numero_autorizacao": "908070", "tipo_cartao": None})
