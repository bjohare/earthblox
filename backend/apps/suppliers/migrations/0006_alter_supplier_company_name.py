# Generated by Django 3.2 on 2022-02-06 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('suppliers', '0005_auto_20220206_1042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='company_name',
            field=models.CharField(max_length=150, unique=True, verbose_name='Company Name'),
        ),
    ]
