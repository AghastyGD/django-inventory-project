# Generated by Django 3.2.21 on 2023-10-03 10:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0006_alter_product_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(choices=[('Electrônicos', 'Eletrônicos'), ('Comida', 'Comida'), ('Livros', 'Livros'), ('Imovéis', 'Imovéis')], max_length=20, null=True),
        ),
    ]
