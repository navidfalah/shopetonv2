# Generated by Django 3.2.12 on 2022-03-30 18:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0018_product_final_price'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='final_price',
            new_name='last_price',
        ),
    ]
