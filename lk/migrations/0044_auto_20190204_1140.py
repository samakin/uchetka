# Generated by Django 2.1.5 on 2019-02-04 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0043_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetal',
            name='photo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='lk.Photo'),
            preserve_default=False,
        ),
    ]
