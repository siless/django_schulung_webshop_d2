# Generated by Django 2.1.2 on 2018-10-30 10:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='article_nr',
            new_name='product_nr',
        ),
    ]
