from django.contrib import admin

# Register your models here.
from .models import Banner ,Category, Marca, Color, Size, Product, ProductAttribute

admin.site.register(Banner)
admin.site.register(Marca)
admin.site.register(Size)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_tag_path')

admin.site.register(Category, CategoryAdmin)






class ColorAdmin(admin.ModelAdmin):
    list_display = ('title', 'color_tag_path')

admin.site.register(Color, ColorAdmin)





class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'marca', 'color', 'size', 'status')
    list_editable = ('status',)

admin.site.register(Product, ProductAdmin)



class ProductAttributeAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'price', 'color', 'size')

admin.site.register(ProductAttribute, ProductAttributeAdmin)