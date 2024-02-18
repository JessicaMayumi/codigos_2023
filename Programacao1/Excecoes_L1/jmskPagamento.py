import abc

class Pagamento(abc.ABC):
    @abc.abstractmethod
    def realizar_pagamento(self):
        pass
