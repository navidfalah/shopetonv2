# Generated by Django 3.2.12 on 2022-03-30 18:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0016_auto_20220330_1727'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hits',
            field=models.ManyToManyField(blank=True, related_name='hitsproduct', to='shop.IPAddress', verbose_name='بازدید ها'),
        ),
    ]
