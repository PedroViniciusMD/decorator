from NotificadorBase import NotificadorBase
from NotificadorEmail import NotificadorEmail
from NotificadorFacebook import NotificadorFacebook
from NotificadorSlack import NotificadorSlack
from NotificadorSMS import NotificadorSMS

email = NotificadorEmail(NotificadorBase())

sms = NotificadorSMS(NotificadorBase())

facebook = NotificadorFacebook(NotificadorBase())

slack = NotificadorSlack(NotificadorBase())

#slack.enviar("sua casa está pegando fogo")

email_sms = NotificadorSMS(NotificadorEmail(NotificadorBase()))
email_sms.enviar("sua casa está pegando fogo")
#print("--------------------------------------")
sms_email = NotificadorEmail(NotificadorSMS(NotificadorBase()))
#sms_email.enviar("sua casa está pegando fogo")# a ordem de envelopamento pode importar

'''
NotificadorSMS.enviar()
        ↓
super().enviar()
        ↓
NotificadorDecorator.enviar()
        ↓
self.notificador.enviar()
        ↓
NotificadorEmail.enviar()
        ↓
super().enviar()
        ↓
NotificadorDecorator.enviar()
        ↓
self.notificador.enviar()
        ↓
NotificadorBase.enviar()
        ↓
pass
'''
