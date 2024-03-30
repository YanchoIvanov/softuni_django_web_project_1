from django.db import models


class AskForOffer(models.Model):
    MAX_LENGTH_NAME = 60
    MAX_LENGTH_SUBJECT = 60
    MAX_LENGTH_PHONE_NUMBER = 15

    email = models.EmailField()
    name = models.CharField(max_length=MAX_LENGTH_NAME)
    # TODO - ONLY NUMBERS!
    phone_number = models.CharField(max_length=MAX_LENGTH_PHONE_NUMBER)
    subject = models.CharField(max_length=MAX_LENGTH_SUBJECT)
    message = models.TextField()

    def __str__(self):
        return self.email
