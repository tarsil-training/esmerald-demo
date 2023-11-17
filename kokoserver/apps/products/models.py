from typing import TYPE_CHECKING

import edgy
from esmerald import settings

registry, _ = settings.db_registry

if TYPE_CHECKING:
    from accounts import User


class Product(edgy.Model):
    """
    Product associated with a user.
    """

    user: "User" = edgy.ForeignKey("User", null=False)
    sku: str = edgy.CharField(max_length=255, null=False)

    class Meta:
        registry = registry
