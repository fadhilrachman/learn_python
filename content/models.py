from django.db import models

# Create your models here.
class Content(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    img= models.TextField()
    donation_target_nominal = models.IntegerField()
    donation_target_date = models.DateField(null=True)
    is_active= models.BooleanField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title