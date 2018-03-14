import os
from django.db import models
from django.conf import settings

class RScript(models.Model):
    script = models.FileField(upload_to=settings.STATIC_R)

    @property
    def script_path(self):
        return os.path.basename(self.script.name)