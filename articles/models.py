from django.db import models
import barcode
from io import BytesIO
from barcode.writer import ImageWriter
from django.core.files import File
# Create your models here.

class articles (models.Model):
    nom_article = models.CharField(max_length=100)
    barcode=models.ImageField(upload_to = 'barcode', blank=True)
    commentaire = models.CharField(max_length=100)
    batch_number = models.CharField(max_length=12,null=True,unique=True)
    image=models.ImageField(upload_to = 'images', blank=True)

    def save(self,*args,**kwargs):
        EAN= barcode.get_barcode_class('ean13')
        ean =EAN(f'{self.batch_number}',writer=ImageWriter())
        buffer = BytesIO()
        ean.write(buffer)
        self.barcode.save('barcode.png',File(buffer),save=False)
        return super().save(*args, **kwargs)