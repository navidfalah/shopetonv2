# Generated by Django 4.0.2 on 2022-03-28 15:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_remove_blogmodel_slug'),
        ('shop', '0011_alter_product_product_choice'),
    ]

    operations = [
        migrations.AddField(
            model_name='myshop',
            name='blogs',
            field=models.ManyToManyField(blank=True, null=True, to='blog.blogModel'),
        ),
    ]
