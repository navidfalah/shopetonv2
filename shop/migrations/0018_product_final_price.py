# Generated by Django 3.2.12 on 2022-03-30 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0017_product_hits'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='final_price',
            field=models.IntegerField(default=1, verbose_name='قیمت کالا| با تخفیف'),
            preserve_default=False,
        ),
    ]
