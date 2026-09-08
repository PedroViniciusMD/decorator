from abc import ABC, abstractmethod


#component
class Notificador(ABC):
    @abstractmethod
    def enviar(self, mensagem):
        pass
   