from notificador import (
    Notificador,
    NotificadorFacebook,
    NotificadorSlack,
    NotificadorSMS,
    NotificadorSMSFacebookSlack,
)

# o cliente precisa conhecer qual classe representa exatamente a combinação que ele quer
notificador = Notificador() # e-mail
sms = NotificadorSMS()
facebook = NotificadorFacebook()
slack = NotificadorSlack()
sms_facebook_slack = NotificadorSMSFacebookSlack()

notificador.enviar("sua casa está pegando fogo")
sms.enviar("sua casa está pegando fogo")
facebook.enviar("sua casa está pegando fogo")
slack.enviar("sua casa está pegando fogo")
sms_facebook_slack.enviar("sua casa está pegando fogo")
