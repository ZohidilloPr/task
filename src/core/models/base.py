from django.db import models


class BaseModel(models.Model):
    title = models.CharField(max_length=255, verbose_name="Title")
    description = models.TextField(verbose_name="Description")
    added_at = models.DateTimeField(auto_now_add=True, verbose_name="Added at")

    objects = models.Manager()

    def __str__(self):
        return str(self.title)

    class Meta:
        abstract = True
