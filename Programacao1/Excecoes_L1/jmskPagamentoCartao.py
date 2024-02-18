from jmskPagamento import Pagamento

class PagamentoCartao(Pagamento):
    
    def realizar_pagamento(self):
        return "Pagamento com o cartão de crédito realizado!"