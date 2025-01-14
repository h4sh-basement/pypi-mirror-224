from django.conf import settings
from django.contrib.postgres.fields import ArrayField
from django.core.serializers.json import DjangoJSONEncoder
from django.db import models

from polyaxon.lifecycle import V1Statuses
from polyaxon.polyflow import V1RunEdgeKind


class BaseRunEdge(models.Model):
    downstream = models.ForeignKey(
        "db.Run", on_delete=models.CASCADE, related_name="upstream_edges"
    )
    upstream = models.ForeignKey(
        "db.Run", on_delete=models.CASCADE, related_name="downstream_edges"
    )
    values = models.JSONField(blank=True, null=True)
    kind = models.CharField(
        max_length=6,
        db_index=True,
        choices=V1RunEdgeKind.to_choices(),
        blank=True,
        null=True,
    )
    statuses = (
        models.JSONField(
            encoder=DjangoJSONEncoder,
            blank=True,
            null=True,
        )
        if settings.DB_ENGINE_NAME == "sqlite"
        else ArrayField(
            models.CharField(
                max_length=16,
                choices=V1Statuses.to_choices(),
            ),
            blank=True,
            null=True,
        )
    )

    class Meta:
        abstract = True
