# Generated by Django 3.2.4 on 2023-01-29 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0016_auto_20230129_1455'),
    ]

    operations = [
        migrations.CreateModel(
            name='RubbersBrand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='RubbersSpeedType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RubbersType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20)),
            ],
            options={
                'ordering': ['id'],
            },
        ),
        migrations.AlterModelOptions(
            name='bladestype',
            options={'ordering': ['id']},
        ),
        migrations.CreateModel(
            name='ValueRubbersAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brand', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.rubbersbrand')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.product')),
                ('speed_type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.rubbersspeedtype')),
                ('type', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='store.rubberstype')),
            ],
            options={
                'verbose_name': 'Value Rubber Attribute',
                'verbose_name_plural': 'Values Rubbers Attributes',
                'ordering': ['id'],
            },
        ),
        migrations.CreateModel(
            name='RubbersProductAttribute',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(db_index=True, max_length=100, verbose_name='Name')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.categoryproduct', verbose_name='Category')),
            ],
            options={
                'verbose_name': 'Rubber Attribute',
                'verbose_name_plural': 'Rubbers Attributes',
                'ordering': ['id'],
            },
        ),
    ]
