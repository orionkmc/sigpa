from django.contrib.contenttypes.models import ContentType
from django.contrib.admin.models import LogEntry, ADDITION, CHANGE, DELETION


class AuditMixin(object):
    def save_log(self, user, message, action):
        LogEntry.objects.create(
            user_id=user.pk,
            content_type_id=ContentType.objects.get_for_model(self).pk,
            object_id=str(self.pk),
            object_repr=self,
            action_flag=action,
            change_message=message
        )

    def save_addition(self, user):
        message = 'Añadido'
        self.save_log(user, message, ADDITION)

    def save_edition(self, user):
        self.save_log(user, 'Cambiado', CHANGE)

    def save_deletion(self, user):
        self.save_log(user, 'Eliminado', DELETION)
