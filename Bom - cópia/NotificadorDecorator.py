from Notificador import Notificador


# base decorator
class NotificadorDecorator(Notificador):
    def __init__(self, notificador: Notificador):
        self.notificador = notificador
    
    def enviar(self, mensagem):
        self.notificador.enviar(mensagem)
        