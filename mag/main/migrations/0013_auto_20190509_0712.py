# Generated by Django 2.2 on 2019-05-09 07:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20190509_0534'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='recipe',
            name='comments',
        ),
        migrations.AddField(
            model_name='comments',
            name='recipe',
            field=models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='main.Recipe'),
        ),
    ]
