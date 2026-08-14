from django.db import models

# Create your models here.
class Message(models.Model):
    owner = models.CharField(max_length=20)
    msg_text = models.CharField(max_length=200)
    timestamp = models.DateTimeField('message timestamp')
    def __str__(self):
        return self.msg_text