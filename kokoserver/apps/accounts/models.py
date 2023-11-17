import edgy
from esmerald import settings
from esmerald.contrib.auth.edgy.base_user import AbstractUser

registry, _ = settings.db_registry


class User(AbstractUser):
    """
    Base User
    """

    middle_name: str = edgy.CharField(max_length=255, null=True)

    class Meta:
        registry = registry
