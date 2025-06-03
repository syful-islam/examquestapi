from django.core.management.base import BaseCommand
from datetime import date
from app.modules.general_module.models.notification import Notification
from app.modules.sam.models.contract import Contract
from app.modules.utils.email_utility import EmailService
from app.core.logger import log
from django.utils import timezone
from datetime import datetime

class Command(BaseCommand):
    help = 'Generate contract renewal notifications'

    def handle(self, *args, **kwargs):
        today = date.today()
        contracts = Contract.objects.filter(
            reminder_date__lte=today,
            ref_contract_id__isnull=True,
        ).exclude(status='archived')

        for contract in contracts:
            user = contract.owner
            if not user:
                continue

            already_exists = Notification.objects.filter(
                user=user,
                target_type='contract',
                target_id=contract.id,
                #title__icontains='Renewal Reminder',
                created_at__date=today
            ).exists()

            if not already_exists:
                Notification.objects.create(
                    user=user,
                    subscriber=contract.subscriber,
                    title=f'{contract.title}',
                    message=f'Contract with {contract.supplier} is due for renewal',
                    category=contract.category,
                    supplier=contract.supplier,
                    expiry_date=timezone.make_aware(
                            datetime.combine(contract.end_date, datetime.min.time())
                        ) if timezone.is_naive(datetime.combine(contract.end_date, datetime.min.time())) else contract.end_date,
                        target_type='contract',
                    target_id=contract.id,
                    target_url=f'/contracts/{contract.id}/',
                    is_read=False
                )
        self.stdout.write(self.style.SUCCESS('Reminder notifications generated.'))

        notifications = Notification.objects.filter(
            user=user,
            target_type='contract',
            #target_id=contract.id,
            #title__icontains='Renewal Reminder',
            created_at__date=today
        )
        if not notifications.exists():
            self.stdout.write(self.style.WARNING('No notifications to send.'))
            return

        # Prepare email content
        context = {
            "user_name": user.full_name,
            "email_title": "Contract Renewal Reminder",
            "notifications": notifications,
        }

        to_email = user.email
        self.send_reminder_email(to_email, context)
        self.stdout.write(self.style.SUCCESS('Reminder notifications email send.'))
        log.info(f"Notification created and email sent to {user.email} for contract {contract.contract_no}")

    def send_reminder_email(self, to_email, context):
        email_service = EmailService()
        success = email_service.send_contract_reminder_email(
            to_email=to_email,
            context=context,
        )

        if success:
            log.info(f"Notification email sent to {to_email}")
        else:
            log.error(f"Failed to send notification email to {to_email}")