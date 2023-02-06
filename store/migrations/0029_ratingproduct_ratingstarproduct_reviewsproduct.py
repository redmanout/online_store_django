# Generated by Django 3.2.4 on 2023-02-05 14:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0028_auto_20230204_1504'),
    ]

    operations = [
        migrations.CreateModel(
            name='RatingStarProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.PositiveIntegerField(default=0)),
            ],
            options={
                'verbose_name': 'Rating Star',
                'verbose_name_plural': 'Rating Stars',
            },
        ),
        migrations.CreateModel(
            name='ReviewsProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254)),
                ('name', models.CharField(max_length=150, verbose_name='Name')),
                ('text', models.TextField(max_length=4000, verbose_name='Message')),
                ('parent', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='store.reviewsproduct', verbose_name='Parent')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product')),
            ],
            options={
                'verbose_name': 'Review',
                'verbose_name_plural': 'Reviews',
            },
        ),
        migrations.CreateModel(
            name='RatingProduct',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ip', models.CharField(max_length=20, verbose_name='Ip')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product', verbose_name='Product')),
                ('star', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.ratingstarproduct', verbose_name='Star')),
            ],
            options={
                'verbose_name': 'Rating',
                'verbose_name_plural': 'Ratings',
            },
        ),
    ]
