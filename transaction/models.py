from django.db import models
from  content.models import Content
# Create your models here.
class Transaction(models.Model):
    name = models.TextField()
    email = models.TextField()
    message = models.TextField()
    donation_nominal = models.IntegerField()
    content = models.ForeignKey(Content, on_delete=models.CASCADE, related_name='Transactions')

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name