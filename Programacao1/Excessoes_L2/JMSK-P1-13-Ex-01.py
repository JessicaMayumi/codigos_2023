import abc

class Transacao(abc.ABC):
    @abc.abstractmethod
    def realizar_transacao(self):
        pass
    
class TransferenciaBancaria(Transacao):
    def realizar_transacao(self):
        return "Transferencia Bancária realizada! "

class PagamentoDebito(Transacao):
    def realizar_transacao(self):
        return "Pagamento com cartão de débito realizado! "

class PagamentoApp(Transacao):
    def realizar_transacao(self):
        return "Pagamento via Aplicativo realizado! "
    
def processar_transacao(transacao):
    return transacao.realizar_transacao()

try:
    tb = TransferenciaBancaria()
    td = PagamentoDebito()
    ta = PagamentoApp()
    print(processar_transacao(tb))
    print(processar_transacao(tb))
    print(processar_transacao(ta))

except:
    print("Ocorreu algum erro! ")
    
