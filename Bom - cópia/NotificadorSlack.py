from NotificadorDecorator import NotificadorDecorator


class NotificadorSlack(NotificadorDecorator):
    def enviar(self, mensagem):
        super().enviar(mensagem)
        print(f"enviando via slack: {mensagem}")
