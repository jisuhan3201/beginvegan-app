from django.db import models
from beginvegan_app.materials import models as material_models
from django.utils.html import format_html

# Create your models here.
class TimeStampedModel(models.Model):

    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        abstract = True

class ProductCategory(TimeStampedModel):

    name = models.CharField(max_length=100, null=True, blank=True)
    sub_category = models.ForeignKey('self', on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'product_categories'

# class ProductSubCategory(models.Model):

#     name = models.CharField(max_length=100, null=True, blank=True)
#     parent_category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, related_name="parent_category")
#     updated_at = models.DateTimeField(auto_now=True, null=True)

#     def __str__(self):
#         return "{}".format(self.name)

#     class Meta:
#         db_table = 'product_subcategories'


class Company(TimeStampedModel):

    name = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'companies'


class Product(TimeStampedModel):

    name = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(ProductCategory, on_delete=models.SET_NULL, null=True, blank=True, related_name="category")
    materials = models.ManyToManyField(material_models.Material, through="ProductMaterial", related_name="materials")
    company = models.ForeignKey(Company, on_delete=models.SET_NULL, null=True, blank=True, related_name="company")
    remove_materials = models.ManyToManyField(material_models.Material, through="RemoveMaterial", related_name="remove_materials")

    def __str__(self):
        return "{}".format(self.name)

    class Meta:
        db_table = 'products'


class ProductMaterial(TimeStampedModel):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="pm_product")
    material = models.ForeignKey(material_models.Material, on_delete=models.CASCADE, related_name="pm_material")
    
    def __str__(self):
        return "{} - {}".format(self.product, self.material)

    class Meta:
        db_table = 'product_material'


class RemoveMaterial(TimeStampedModel):

    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="rm_product")
    material = models.ForeignKey(material_models.Material, on_delete=models.CASCADE, related_name="rm_material")
    
    def __str__(self):
        return "{} - {}".format(self.product, self.material)

    class Meta:
        db_table = 'remove_material'

class ProductImage(TimeStampedModel):

    title = models.CharField(max_length=255, null=True, blank=True)
    image = models.ImageField(upload_to='img/raw_images', null=True, blank=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        db_table = 'product_images'
