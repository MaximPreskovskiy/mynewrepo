from django.db import models

# Create your models here.

class users(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    ID_access_rights = models.CharField(max_length=10)

class CommNumber(models.Model):
    ID_CommNumber = models.CharField(max_length=100)
    content = models.CharField(max_length=1000)

class AccessRights(models.Model):
    ID_access_rights = models.CharField(max_length=100)
    Rights_Name = models.CharField(max_length=100)

class Orders(models.Model):
    Order_Name = models.CharField(max_length=100)
    ID_CommNumber = models.CharField(max_length=100)

class Documents(models.Model):
    Document_Name = models.CharField(max_length=100)
    File_Path = models.CharField(max_length=100)
    Order_Name =models.CharField(max_length=100)


class Spareparts(models.Model):
    name = models.CharField(max_length=100)
    description = models.CharField(max_length=5000, null=True)
    producer = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    id_num = models.CharField(max_length=100)
    cost = models.FloatField(max_length=100)
    cat = models.ForeignKey("Category", on_delete=models.PROTECT)
    image_name = models.ForeignKey("Images", on_delete=models.PROTECT, null=True)

class Category(models.Model):
    cat = models.CharField(max_length=100)

class Images(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="trp_db/static/pic")