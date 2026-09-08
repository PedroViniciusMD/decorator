from NotificadorDecorator import NotificadorDecorator


class NotificadorEmail(NotificadorDecorator):
    def enviar(self, mensagem):
        super().enviar(mensagem)
        print(f"enviando via e-mail: {mensagem}")
