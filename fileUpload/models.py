from django.db import models

# Create your models here.
from django.db import models


class FilesModel(models.Model):
    name = models.CharField(verbose_name="文件名", max_length=20, default="")
    file = models.FileField(upload_to='uploads/')

    class Meta:
        db_table = 'files_storage'
        ordering = ['-id']
