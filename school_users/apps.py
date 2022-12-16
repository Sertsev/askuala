from django.apps import AppConfig


class SchoolUsersConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'school_users'

    def ready(self) -> None:
        import school_users.signals.handlers