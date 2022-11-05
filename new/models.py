from django.db import models
# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length = 100,null= True)
    email = models.EmailField(max_length = 100,null= True)
    message = models.TextField(max_length = 100,null= True)
    

    def __str__(self) -> str:
        return self.name