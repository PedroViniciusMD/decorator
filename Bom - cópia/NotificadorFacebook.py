from NotificadorDecorator import NotificadorDecorator


class NotificadorFacebook(NotificadorDecorator):
    def enviar(self, mensagem):
        super().enviar(mensagem)
        print(f"enviando via facebook: {mensagem}")
        