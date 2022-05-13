from distutils.command.upload import upload
from django.db import models
from django.utils.text import slugify
from ckeditor.fields import RichTextField


# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(null=False, blank=True, unique=True, db_index=True, editable=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

class Blog(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="blogs")
    description = RichTextField()                   # models.TextField() yerine RichTextField() i kullandik bu description bolumunu html editoru olarak kullanmamizi saglayacak.
    is_active = models.BooleanField(default=False)
    is_home = models.BooleanField(default=False)
    slug = models.SlugField(null=False, unique=True, blank=True, db_index=True, editable=False)           # url de sayilar gormek bazen hos degil, bunun yerine ...
                                                                                                          # blank=True dersek adminde blog degistirirken slug alani zorunlu olmaktan cikar.
                                                                                                          # editable=False yaptik. Adminde yeni bir blog olustururken slug yazamayiz.
                                                                                                          # Otomatik olarak kendisi yapar.      
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    categories = models.ManyToManyField(Category)       #Burda blank=True da eklersek category verme zorunlulugumuz kalkar. (Adminde gorebilirsin, her blog icin kategori girmek zorunlu.)



    def __str__(self):                      # Bu fonksiyonu anlamak icin 
        return f"{self.title}"              # admin de blogs a bak (models 1, 2, 3 yerine isimleri geldi.)


    def save(self, *args, **kwargs):                                         # url de sayilar gormek bazen hos degil, bunun yerine ...
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)


