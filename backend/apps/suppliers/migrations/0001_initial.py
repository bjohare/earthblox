# Generated by Django 3.2 on 2022-02-03 15:12

import django.contrib.postgres.fields
from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Supplier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', model_utils.fields.AutoCreatedField(default=django.utils.timezone.now, editable=False, verbose_name='created')),
                ('modified', model_utils.fields.AutoLastModifiedField(default=django.utils.timezone.now, editable=False, verbose_name='modified')),
                ('company_name', models.CharField(max_length=150)),
                ('contact_name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('datatypes', django.contrib.postgres.fields.ArrayField(base_field=models.CharField(choices=[('GP', 'Geotagged Photos'), ('DP', 'Drone Photography'), ('GC', 'Ground Control Points'), ('DV', 'Drone Video'), ('DL', 'Drone Lidar'), ('DR', 'Drone Radar'), ('AV', 'Aerial Video'), ('AR', 'Aerial Radar'), ('AL', 'Aerial Lidar'), ('AP', 'Aerial Photo'), ('SP', 'Stereo Photo'), ('OT', 'Other')], max_length=2), default=list, size=None)),
            ],
        ),
        migrations.AddIndex(
            model_name='supplier',
            index=models.Index(fields=['company_name'], name='company_name_idx'),
        ),
    ]