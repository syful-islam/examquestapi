from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings
import smtplib
from email.utils import formataddr
from app.core.logger import log

class EmailService:
    def __init__(self):
        self.from_email = settings.EMAIL_HOST_USER
        self.from_name = settings.EMAIL_FROM_NAME
        self.smtp_server = settings.EMAIL_HOST
        self.smtp_port = settings.EMAIL_PORT
        self.smtp_user = settings.EMAIL_HOST_USER
        self.smtp_password = settings.EMAIL_HOST_PASSWORD
        self.default_from_email = settings.DEFAULT_FROM_EMAIL

    def send_email(self, to_email, subject, template_name, context):
        try:
            # Render HTML content
            base_url = settings.BASE_URL
            context['base_url'] = base_url
            context['company_name'] = "Procure Tool"
            context['company_tagline'] = "Simple & Efficient"
            html_content = render_to_string(f'email/{template_name}', context)
            
            # Create email
            # email = EmailMultiAlternatives(
            #     subject=subject,
            #     body=html_content,
            #     from_email = formataddr((self.from_name, self.from_email)),
            #     to=[to_email]
            # )
            email = EmailMultiAlternatives(
                subject=subject,
                body=html_content,
                from_email = formataddr((self.from_name, self.default_from_email)),
                to=[to_email]
            )
            email.attach_alternative(html_content, "text/html")
            
            # Send email
            email.send()
            return True
        except smtplib.SMTPException as e:
            print(f"Email sending failed: {str(e)}")
            log.error(f"Email sending failed: {str(e)}")
            return False

    def send_otp_email(self, to_email, otp, user_name):
        context = {
            'user_name': user_name,
            'otp': otp,
            'validity_minutes': settings.OTP_EXPIRY_MINUTES
        }
        return self.send_email(to_email, "Your OTP Verification Code", "otp_email.html", context)

    def send_contract_reminder_email(self, to_email, context):
        subject = "Notification from Procure Tool"
        if context.get('email_title'):
            subject = subject+' ('+context['email_title']+')'
        return self.send_email(to_email, subject, "contract_reminder_email.html", context)

    def send_report_email(self, to_email, report_data, user_name):
        context = {
            'user_name': user_name,
            'report_data': report_data
        }
        return self.send_email(to_email, "Your Report", "report_email.html", context)