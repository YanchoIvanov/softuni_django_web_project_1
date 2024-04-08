from django.contrib.auth import get_user_model
from django.db import models


UserModel = get_user_model()


class Item(models.Model):
    MAX_LENGTH_TITLE = 50

    title = models.CharField(
        max_length=MAX_LENGTH_TITLE,
    )
    description = models.TextField(

    )
    image = models.ImageField(
        upload_to='item_images/',
    )
    availability = models.BooleanField(
        default=True,
    )
    characteristics = models.TextField(

    )
    created_by = models.ForeignKey(
        to=UserModel,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.title
