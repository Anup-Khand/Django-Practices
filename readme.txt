EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_HOST = "smtp.gmail.com"
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_FROM = "basantkhand20@gmail.com"
EMAIL_HOST_USER = "basantkhand20@gmail.com"
EMAIL_HOST_PASSWORD = "uojqyzzqzmdlrekx"




in terminal
py manage.py shell
email = EmailMessage('subject','body',to=[krishnasapkota57@gmail.com])
email.send()