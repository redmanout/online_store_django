# Generated by Django 3.2.4 on 2023-01-29 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_auto_20230129_1140'),
    ]

    operations = [
        migrations.CreateModel(
            name='ProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='products_attribute', to='store.categoryproduct', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Product Attribute',
                'verbose_name_plural': 'Products Attributes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='ValueProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_attribute', models.CharField(blank=True, max_length=40, verbose_name='Value')),
                ('attribute', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value_product_attribute', to='store.productattribute')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value_product_attribute', to='store.product')),
            ],
        ),
    ]