from jmskPagamento import Pagamento

class PagamentoDinheiro(Pagamento):
    def realizar_pagamento(self):
        return "Pagamento com dinheiro realizado!"