# Generated by Django 3.0.9 on 2020-08-04 13:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20200804_1347'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='is_publised',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='Image',
            field=models.ImageField(upload_to='product/%Y/%m/%d/'),
        ),
    ]