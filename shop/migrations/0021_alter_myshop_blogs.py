# Generated by Django 3.2.12 on 2022-03-31 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_alter_blogmodel_created_alter_blogmodel_modified'),
        ('shop', '0020_alter_product_off'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myshop',
            name='blogs',
            field=models.ManyToManyField(blank=True, to='blog.blogModel'),
        ),
    ]
