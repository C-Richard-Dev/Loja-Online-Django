#from distutils.command.upload import upload
from django.db import models
from django.utils.html import mark_safe

# Create your models here.


class Banner(models.Model):
    img = models.CharField(max_length=250)
    alt_text = models.CharField(max_length=300)

    class Meta:
        verbose_name_plural = "1. Banners"


class Category (models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to="ctg_imgs/")

    class Meta:
        verbose_name_plural = "2. Categories"


    def image_tag_path(self):
        return mark_safe('<img src="%s" width="50" height="50" />' %(self.image.url))

    def __str__(self):
        return self.title


class Marca(models.Model):
    title = models.CharField(max_length=30)
    image = models.ImageField(upload_to="marca_imgs/", null=True, blank=True)

    class Meta:
        verbose_name_plural = "3. Marcas"


    def image_tag_path(self):
        return mark_safe('<img src="%s" width="50" height="120" />' %(self.image.url))

    def __str__(self):
        return self.title
    

class Color(models.Model):
    title = models.CharField(max_length=100)
    color_code = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "4. Colors"

    def color_tag_path(self):
        return mark_safe('<div style =" width:50px; height:120px; background:%s" </div>' %(self.color_code))

    def __str__(self):
        return self.title
    

class Size(models.Model):
    title = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = "5. Sizes"
    
    def __str__(self):
        return self.title
    

class Product(models.Model):
    title = models.CharField(max_length=200)
    image = models.ImageField(upload_to="product_imgs/")
    slug = models.CharField(max_length=300)
    detail = models.TextField()
    specs = models.TextField()
    marca = models.ForeignKey(Marca,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "6. Products"

    def __str__(self):
        return self.title
    


class ProductAttribute(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.ForeignKey(Color,on_delete=models.CASCADE)
    size = models.ForeignKey(Size,on_delete=models.CASCADE)
    price = models.PositiveIntegerField()

    class Meta:
        verbose_name_plural = "7. ProductAttributes"

    def __str__(self):
        return self.product.title
