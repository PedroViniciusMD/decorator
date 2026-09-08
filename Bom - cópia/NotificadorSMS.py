from NotificadorDecorator import NotificadorDecorator


class NotificadorSMS(NotificadorDecorator):
    def enviar(self, mensagem):
        super().enviar(mensagem)
        print(f"enviando via SMS: {mensagem}")
