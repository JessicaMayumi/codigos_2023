from jmskPagamento import Pagamento
from jmskPagamentoCartao import PagamentoCartao
from jmskPagamentoCheque import PagamentoCheque
from jmskPagamentoDinheiro import PagamentoDinheiro

def processar_pagamento(pagamento):
    return pagamento.realizar_pagamento()
    
try:
    p1 = PagamentoCartao()
    p2 = PagamentoCheque()
    p3 = PagamentoDinheiro()

#print(p1.realizar_pagamento())

    print(processar_pagamento(p1))
    print(processar_pagamento(p2))
    print(processar_pagamento(p3))
       
except:
    print("Algo deu errado. Insira um valor válido!")

#else:
    print("Obrigado! Volte sempre!")