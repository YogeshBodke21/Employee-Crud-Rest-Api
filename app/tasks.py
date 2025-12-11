from celery import shared_task
from django.core.mail import send_mail
from EMP_MGM import settings
from django.core.mail import send_mail, EmailMultiAlternatives

@shared_task
def send_html_mail_task(email, html_content):
     msg = EmailMultiAlternatives(
     "Registeration has been done!",
     "Welcome to Django based Application.",
     settings.EMAIL_HOST_USER,
     [email],
     headers={"List-Unsubscribe": email},
     )
     msg.attach_alternative(html_content, "text/html")
     msg.send()
     return "done"

@shared_task
def send_mail_to_manager(manager_email, html_content):
     msg = EmailMultiAlternatives(
     "New employee has been added!",
     "Email with celery",
     settings.EMAIL_HOST_USER,
     [manager_email],
     headers={"List-Unsubscribe": manager_email},
     )
     msg.attach_alternative(html_content, "text/html")
     msg.send()
     return "done"