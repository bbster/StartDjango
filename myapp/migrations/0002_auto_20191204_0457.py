# Generated by Django 2.2.7 on 2019-12-03 19:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='picture',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
