from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from app.modules.general_module.models.audit_log import AuditLog
from app.middleware.ThreadLocalMiddleware import get_app_user
from app.core.logger import log

def track_model_changes(sender, instance, fields_to_track, **kwargs):
    log.info(f"Tracking changes for {sender.__name__} with instance: {instance}")
    if instance.pk:  # Only for updates, not creates
        old_instance = sender.objects.get(pk=instance.pk)
        changes = {}
        user = get_app_user()

        for field in fields_to_track:
            old_value = getattr(old_instance, field)
            new_value = getattr(instance, field)
            if old_value != new_value:
                changes[field] = {
                    "from": str(old_value),
                    "to": str(new_value)
                }

        if changes:
            AuditLog.objects.create(
                resource_name=sender.__name__,
                object_id=str(instance.pk),
                action='Updated',
                changes=changes,
                notes='Changed fields: ' + ', '.join(changes.keys()),
                user_id=user.id if user else None,
                subscriber_id=getattr(instance, 'subscriber_id', None)
            )

# @receiver(pre_save, sender=Contract)
# def track_contract_changes(sender, instance, **kwargs):
#     track_model_changes(sender, instance, fields_to_track=['title', 'start_date','end_date','owner'], **kwargs)

