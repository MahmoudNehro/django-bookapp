from django.db import models

from author.models import Author

# Create your models here.
class Book(models.Model):
    name=models.CharField(max_length=250)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, null=True)
    published_at=models.DateTimeField()
    add_to_site=models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    appropriate=models.CharField(max_length=250,choices=[("8","Kid"),("8-15","teenager"),("15+","adult")],default="adult")
    image = models.ImageField (max_length=255, upload_to="img/%y",null=True)

    def __str__(self):
        return self.name