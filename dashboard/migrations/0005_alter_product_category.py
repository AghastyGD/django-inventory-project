# Generated by Django 3.2.21 on 2023-10-03 09:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0004_auto_20231003_0656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electronics', 'Eletrônicos'), ('Food', 'Comida'), ('Book', 'Livros')], max_length=20, null=True),
        ),
    ]
