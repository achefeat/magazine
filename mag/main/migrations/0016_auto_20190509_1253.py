# Generated by Django 2.2 on 2019-05-09 12:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20190509_0806'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, related_name='asd', to='main.Recipe'),
        ),
    ]
