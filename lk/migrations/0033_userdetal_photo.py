# Generated by Django 2.1.5 on 2019-01-30 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0032_stock_account'),
    ]

    operations = [
        migrations.AddField(
            model_name='userdetal',
            name='photo',
            field=models.ImageField(default='', upload_to='detals'),
            preserve_default=False,
        ),
    ]
