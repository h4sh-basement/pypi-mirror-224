from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models


class TagModel(models.Model):
    # Special handing for sqlite without migrating previous installation using ArrayField
    tags = (
        models.JSONField(
            encoder=DjangoJSONEncoder,
            blank=True,
            null=True,
        )
        if settings.DB_ENGINE_NAME == "sqlite"
        else ArrayField(
            base_field=models.CharField(max_length=64), blank=True, null=True
        )
    )

    class Meta:
        abstract = True
