from django.db import models
from influencer.utils import get_uuid

# Create your models here.

# class ProductCategory(models.Model):
#     name = models.CharField(max_length=255, unique=True)
#     description = models.CharField(max_length=255, blank=True, null=True)

#     class Meta:
#         db_table = "category"
#         ordering = ["name"]

#     def __str__(self):
#         return self.name

#     def save(self, **kwargs):
#         return super().save(**kwargs)


# class Product(models.Model):
#     quantity = models.IntegerField(default=0)
#     name = models.CharField(max_length=255)
#     code = models.CharField(max_length=10, unique=True)
#     category = models.name = models.ForeignKey(
#         ProductCategory, related_name='categories', on_delete=models.CASCADE
#     )

#     class Meta:
#         db_table = "product"
#         ordering = ["-id"]

#     def __str__(self):
#         return self.name

#     def save(self, **kwargs):
#         return super().save(**kwargs)

#     @staticmethod
#     def generate_bsin(code):
#         gr_code = get_uuid(prefix=f"N{code}", length=5)
#         while Product.include_deleted.filter(code=gr_code).exists():
#             code = Product.generate_bsin(code)
#         return code
