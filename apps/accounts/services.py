from django.core.mail import send_mail
from django.conf import settings
from django.utils.crypto import get_random_string

def generate_verification_token():
    return get_random_string(64)

def send_verification_email(user, token):
    verification_link = f"http://localhost:8000/accounts/verify-email/?token={token}"
    subject = "E-posta Doğrulama"
    message = f"Merhaba {user.username},\n\nLütfen e-postanızı doğrulamak için bu bağlantıya tıklayın:\n{verification_link}"
    
    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [user.email])

def is_corporate_email(email):
    # Gmail gibi genel uzantıları engelle
    general_domains = ["gmail.com", "yahoo.com", "hotmail.com", "outlook.com"]
    domain = email.split("@")[-1]
    return domain not in general_domains
