# Generated by Django 2.1.5 on 2019-02-04 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0044_auto_20190204_1140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
