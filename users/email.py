from django.core.mail import send_mail
from users.jwt import generate_confirm_token
from config import settings

def send_confirm_email(user):
    token = generate_confirm_token(user_id=user.id)
    link = settings.TOKEN_URL + token

    send_mail(
        'Confirm Registration',  
        f'Follow the link: {link}', 
        'from@example.com',
        [user.email],
        fail_silently=False,
    )