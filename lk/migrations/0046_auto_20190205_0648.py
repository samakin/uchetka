# Generated by Django 2.1.5 on 2019-02-05 06:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0045_auto_20190204_1149'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userdetal',
            name='photo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='lk.Photo'),
        ),
    ]
