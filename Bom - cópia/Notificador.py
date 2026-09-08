from abc import ABC, abstractmethod


#component - interface
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass
   