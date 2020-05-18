from django.db import models

# Create your models here.
class Product(models.Model):
    productName = models.CharField(default="",max_length=200)
    price = models.DecimalField(default=0.0, decimal_places=2,max_digits=15)
    description = models.TextField(default="", blank=True)
    image = models.ImageField(upload_to='uploads/',null=True,width_field="width",height_field="height")
    summary = models.TextField(default="", help_text="内容説明を入力してください")
    width = models.IntegerField(default=64)
    height = models.IntegerField(default=64)
    def __str__(self):
        return f'id={self.id} productName={self.productName}'
    