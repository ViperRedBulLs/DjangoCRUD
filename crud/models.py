from django.db import models

class Bio(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    address = models.TextField()
    
    def __str__(self) -> str:
        return str(self.full_name)