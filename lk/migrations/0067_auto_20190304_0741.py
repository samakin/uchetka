# Generated by Django 2.1.5 on 2019-03-04 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lk', '0066_auto_20190304_0720'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autogeneration',
            name='model',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='lk.AutoModel'),
        ),
    ]