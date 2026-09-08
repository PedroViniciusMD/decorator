class Notificador:
    def enviar(self, mensagem):
        print(f"enviando via e-mail: {mensagem}")

class NotificadorSMS(Notificador):
    def enviar(self, mensagem):
        print(f"enviando via SMS: {mensagem}")
        
class NotificadorFacebook(Notificador):
    def enviar(self, mensagem):
        print(f"enviando via facebook: {mensagem}")
        
class NotificadorSlack(Notificador):
    def enviar(self, mensagem):
        print(f"enviando via slack: {mensagem}")
        
class NotificadorSMSFacebookSlack(Notificador):
    def enviar(self, mensagem):
        print(f"enviando via SMS: {mensagem}")
        print(f"enviando via facebook: {mensagem}")
        print(f"enviando via slack: {mensagem}")


# Email + SMS
# Email + Slack
# Email + Facebook
# SMS + Slack
# SMS + Facebook
# Slack + Facebook

# Email + SMS + Slack
# Email + SMS + Facebook
# Email + Slack + Facebook

# Email + SMS + Slack + Facebook

# --> e se o cliente preferir receber a mensagem via WhatsApp?
# WhatsApp
# Email + WhatsApp
# SMS + WhatsApp
# Facebook + WhatsApp
# Slack + WhatsApp
# Email + SMS + WhatsApp
# Email + Slack + WhatsApp
# ...