# Generated by Django 2.2 on 2019-05-08 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20190508_1419'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='photo',
            field=models.ImageField(default=None, null=True, upload_to='images'),
        ),
    ]