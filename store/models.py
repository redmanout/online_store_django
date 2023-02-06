from django.db import models
from autoslug import AutoSlugField
from django.urls import reverse


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


def get_upload_path(instance, filename):
    return "main-block/product/{0}/{1}/{2}".format(instance.category, instance.name, filename).lower()


class Product(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        verbose_name='Category',
        related_name='category',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=200,
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
    bestseller = models.BooleanField(
        verbose_name='Bestseller',
        default=True,
    )
    new = models.BooleanField(
        verbose_name='New',
        default=True,
    )
    stock = models.BooleanField(
        verbose_name='Stock',
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
    image = models.ImageField(
        blank=True,
        upload_to=get_upload_path,
    )

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Product'
        verbose_name_plural = 'Products'


class BladesProductAttribute(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        verbose_name='Category',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        db_index=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Blade Attribute'
        verbose_name_plural = 'Blades Attributes'


class BladesBrand(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class BladesType(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class BladesHandleType(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class BladesComposition(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class BladesSize(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class ValueBladesAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        related_name='blade_attribute',
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        BladesBrand,
        on_delete=models.CASCADE,
        default=None,
    )
    type = models.ForeignKey(
        BladesType,
        on_delete=models.CASCADE,
        default=None,
    )
    handle_type = models.ForeignKey(
        BladesHandleType,
        on_delete=models.CASCADE,
        default=None,
    )
    composition = models.ForeignKey(
        BladesComposition,
        on_delete=models.CASCADE,
        default=None,
    )
    size = models.ForeignKey(
        BladesSize,
        on_delete=models.CASCADE,
        default=None,
    )

    def __str__(self):
        return f'{self.product} {self.brand} {self.type} {self.handle_type} {self.composition} {self.size}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Value Blades Attribute'
        verbose_name_plural = 'Values Blades Attributes'


class RubbersProductAttribute(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        verbose_name='Category',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        db_index=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Rubber Attribute'
        verbose_name_plural = 'Rubbers Attributes'


class RubbersBrand(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class RubbersType(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class RubbersSpeedType(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class ValueRubbersAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        RubbersBrand,
        on_delete=models.CASCADE,
        default=None,
    )
    type = models.ForeignKey(
        RubbersType,
        on_delete=models.CASCADE,
        default=None,
    )
    speed_type = models.ForeignKey(
        RubbersSpeedType,
        on_delete=models.CASCADE,
        default=None,
    )

    def __str__(self):
        return f'{self.product} {self.brand} {self.type} {self.speed_type}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Value Rubber Attribute'
        verbose_name_plural = 'Values Rubbers Attributes'


class BallsProductAttribute(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        verbose_name='Category',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        db_index=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Ball Attribute'
        verbose_name_plural = 'Balls Attributes'


class BallsBrand(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class BallsRank(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class BallsPackage(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class ValueBallsAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        BallsBrand,
        on_delete=models.CASCADE,
        default=None,
    )
    rank = models.ForeignKey(
        BallsRank,
        on_delete=models.CASCADE,
        default=None,
    )
    package = models.ForeignKey(
        BallsPackage,
        on_delete=models.CASCADE,
        default=None,
    )

    def __str__(self):
        return f'{self.product} {self.brand} {self.rank} {self.package}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Value Ball Attribute'
        verbose_name_plural = 'Values Balls Attributes'


class BackpacksBagsProductAttribute(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        verbose_name='Category',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        db_index=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Backpack and Bag Attribute'
        verbose_name_plural = 'Backpacks and Bags Attributes'


class BackpacksBagsBrand(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class BackpacksBagsType(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class BackpacksBagsColor(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class ValueBackpacksBagsAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        BackpacksBagsBrand,
        on_delete=models.CASCADE,
        default=None,
    )
    type = models.ForeignKey(
        BackpacksBagsType,
        on_delete=models.CASCADE,
        default=None,
    )
    color = models.ForeignKey(
        BackpacksBagsColor,
        on_delete=models.CASCADE,
        default=None,
    )

    def __str__(self):
        return f'{self.product} {self.brand} {self.type} {self.color}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Value Backpack and Bag Attribute'
        verbose_name_plural = 'Values Backpacks and Bags Attributes'


class NetsProductAttribute(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        verbose_name='Category',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        db_index=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Net Attribute'
        verbose_name_plural = 'Nets Attributes'


class NetsBrand(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class NetsColor(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class ValueNetsAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        NetsBrand,
        on_delete=models.CASCADE,
        default=None,
    )
    color = models.ForeignKey(
        NetsColor,
        on_delete=models.CASCADE,
        default=None,
    )

    def __str__(self):
        return f'{self.product} {self.brand} {self.color}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Value Net Attribute'
        verbose_name_plural = 'Values Nets Attributes'


class TablesProductAttribute(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        verbose_name='Category',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        db_index=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Table Attribute'
        verbose_name_plural = 'Tables Attributes'


class TablesBrand(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class TablesSection(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class TablesColor(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class TablesThickness(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class ValueTablesAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        TablesBrand,
        on_delete=models.CASCADE,
        default=None,
    )
    section = models.ForeignKey(
        TablesSection,
        on_delete=models.CASCADE,
        default=None,
    )
    color = models.ForeignKey(
        TablesColor,
        on_delete=models.CASCADE,
        default=None,
    )
    thickness = models.ForeignKey(
        TablesThickness,
        on_delete=models.CASCADE,
        default=None,
    )

    def __str__(self):
        return f'{self.product} {self.brand} {self.section} {self.color} {self.thickness}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Value Table Attribute'
        verbose_name_plural = 'Values Tables Attributes'


class RacketsProductAttribute(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        verbose_name='Category',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        db_index=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Racket Attribute'
        verbose_name_plural = 'Rackets Attributes'


class RacketsBrand(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class RacketsType(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class RacketsHandleType(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class RacketsAverageWeight(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class RacketsRubbersThickness(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class ValueRacketsAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        RacketsBrand,
        on_delete=models.CASCADE,
        default=None,
    )
    type = models.ForeignKey(
        RacketsType,
        on_delete=models.CASCADE,
        default=None,
    )
    handle_type = models.ForeignKey(
        RacketsHandleType,
        on_delete=models.CASCADE,
        default=None,
    )
    average_weight = models.ForeignKey(
        RacketsAverageWeight,
        on_delete=models.CASCADE,
        default=None,
    )
    rubbers_thickness = models.ForeignKey(
        RacketsRubbersThickness,
        on_delete=models.CASCADE,
        default=None,
    )

    def __str__(self):
        return f'{self.product} {self.brand} {self.type} {self.handle_type} {self.average_weight} {self.rubbers_thickness}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Value Racket Attribute'
        verbose_name_plural = 'Values Rackets Attributes'


class AccessoriesProductAttribute(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        verbose_name='Category',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        verbose_name='Name',
        max_length=100,
        db_index=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['id']
        verbose_name = 'Accessorie Attribute'
        verbose_name_plural = 'Accessories Attributes'


class AccessoriesBrand(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title


class AccessoriesType(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class AccessoriesColor(models.Model):
    title = models.CharField(max_length=20)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['id']


class ValueAccessoriesAttribute(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
    )
    brand = models.ForeignKey(
        AccessoriesBrand,
        on_delete=models.CASCADE,
        default=None,
    )
    type = models.ForeignKey(
        AccessoriesType,
        on_delete=models.CASCADE,
        default=None,
    )
    color = models.ForeignKey(
        AccessoriesColor,
        on_delete=models.CASCADE,
        default=None,
    )

    def __str__(self):
        return f'{self.product} {self.brand} {self.type} {self.color}'

    class Meta:
        ordering = ['id']
        verbose_name = 'Value Accessory Attribute'
        verbose_name_plural = 'Values Accessories Attributes'


class Images(models.Model):
    category = models.ForeignKey(
        CategoryProduct,
        on_delete=models.CASCADE,
        default=None,

    )
    product = models.ForeignKey(
        Product,
        related_name='images_product',
        on_delete=models.CASCADE,
    )
    name = models.CharField(
        max_length=200,
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


class RatingStarProduct(models.Model):
    value = models.PositiveIntegerField(default=0)

    def __str__(self):
        return self.value

    class Meta:
        verbose_name = 'Rating Star'
        verbose_name_plural = 'Rating Stars'


class RatingProduct(models.Model):
    ip = models.CharField(
        verbose_name='Ip',
        max_length=20,
    )
    star = models.ForeignKey(
        RatingStarProduct,
        on_delete=models.CASCADE,
        verbose_name='Star',
    )
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        verbose_name='Product',
    )

    def __str__(self):
        return f'{self.star} - {self.product}'

    class Meta:
        verbose_name = 'Rating'
        verbose_name_plural = 'Ratings'


class ReviewsProduct(models.Model):
    email = models.EmailField()
    name = models.CharField(
        verbose_name='Name',
        max_length=150,
    )
    text = models.TextField(
        verbose_name='Message',
        max_length=4000,
    )
    parent = models.ForeignKey(
        'self',
        verbose_name='Parent',
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    product = models.ForeignKey(
        Product,
        verbose_name='Product',
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'{self.name} - {self.product}'

    class Meta:
        verbose_name = 'Review'
        verbose_name_plural = 'Reviews'
