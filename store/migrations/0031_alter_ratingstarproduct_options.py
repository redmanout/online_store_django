# Generated by Django 3.2.4 on 2023-02-17 16:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0030_alter_reviewsproduct_product'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='ratingstarproduct',
            options={'ordering': ['-value'], 'verbose_name': 'Rating Star', 'verbose_name_plural': 'Rating Stars'},
        ),
    ]
