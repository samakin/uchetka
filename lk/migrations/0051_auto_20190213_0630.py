# Generated by Django 2.1.5 on 2019-02-13 06:30

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0050_autodetalsubgrouplevel1'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='autodetalsubgrouplevel1',
            name='main_group',
        ),
        migrations.DeleteModel(
            name='AutoDetalMainGroup',
        ),
        migrations.DeleteModel(
            name='AutoDetalSubgroupLevel1',
        ),
    ]
