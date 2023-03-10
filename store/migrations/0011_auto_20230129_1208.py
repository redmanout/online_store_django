# Generated by Django 3.2.4 on 2023-01-29 12:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_auto_20230129_1206'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bladesproductattribute',
            options={'ordering': ['id'], 'verbose_name': 'Blade Attribute', 'verbose_name_plural': 'Blades Attributes'},
        ),
        migrations.AlterModelOptions(
            name='valuebladesattribute',
            options={'ordering': ['id'], 'verbose_name': 'Value Blades Attribute', 'verbose_name_plural': 'Values Blades Attributes'},
        ),
        migrations.AlterField(
            model_name='bladesproductattribute',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='blades_attribute', to='store.categoryproduct', verbose_name='Category'),
        ),
        migrations.AlterField(
            model_name='valuebladesattribute',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='value_blades_attribute', to='store.product'),
        ),
    ]
