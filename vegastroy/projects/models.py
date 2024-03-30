from django.db import models


class Project(models.Model):
    MAX_LENGTH_TITLE = 100

    title = models.CharField(max_length=MAX_LENGTH_TITLE)
    description = models.TextField()
    image = models.FileField(upload_to="project_images/", blank=True)

