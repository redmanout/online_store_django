from django.db import models
from autoslug import AutoSlugField


# Create your models here.

class CategoryProduct(models.Model):
    name = models.CharField(
        max_length=120,
        db_index=True,
        verbose_name='Category name',
        unique=True,
    )
    slug = AutoSlugField(
        populate_from='name',
        max_length=150,
        unique=True,
        db_index=True,
        null=True,
        default=None,
    )
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name='Date of creation',
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name='Date of change',
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Product(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        verbose_name='Category',
        related_name='products',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        db_index=True,
    )
    slug = AutoSlugField(
        populate_from='name',
        max_length=150,
        unique=True,
        db_index=True,
        null=True,
        default=None,
    )
    description = models.TextField(
        verbose_name='Description',
        blank=True,
    )
    characteristics = models.TextField(
        verbose_name='Characteristics',
        blank=True,
    )
    available_status = models.BooleanField(
        verbose_name='Available status',
        default=True,
    )
    quantity_in_stock = models.PositiveIntegerField(
        verbose_name='Quantity in stock',
        default=0,
    )
    price = models.DecimalField(
        verbose_name='Price',
        max_digits=10,
        decimal_places=2,
    )
    created_at = models.DateTimeField(
        verbose_name='Created at',
        auto_now_add=True,
    )
    updated_at = models.DateTimeField(
        verbose_name='Updated at',
        auto_now=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


def get_upload_path(instance, filename):
    return "main-block/product/{0}/{1}/{2}".format(instance.category, instance.name, filename).lower()


class Images(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        on_delete=models.CASCADE,
        default=None,
        related_name='images_products'
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=40,
        blank=True,
        verbose_name='Name',
    )
    image = models.ImageField(
        blank=True,
        upload_to=get_upload_path,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Image'
        verbose_name_plural = 'Images'
