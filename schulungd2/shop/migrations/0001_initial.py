# Generated by Django 2.1.2 on 2018-10-30 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('description_short', models.TextField()),
                ('description_long', models.TextField()),
                ('article_nr', models.CharField(max_length=254, unique=True)),
                ('count', models.IntegerField()),
                ('weight', models.FloatField()),
                ('product_img', models.ImageField(upload_to='')),
            ],
        ),
    ]