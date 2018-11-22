from django.db import models

class CMSBlock(models.Model):
    id = models.CharField(max_length=25, primary_key=True)
    content = models.TextField()

    def __str__(self):
        return self.id
