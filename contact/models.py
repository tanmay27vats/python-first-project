from django.db import models


class Contact(models.Model):
    full_name = models.CharField(max_length=255)
    email = models.EmailField()
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    # def __str__(self):
    #     return self.email
    def __int__(self):
        return self.id