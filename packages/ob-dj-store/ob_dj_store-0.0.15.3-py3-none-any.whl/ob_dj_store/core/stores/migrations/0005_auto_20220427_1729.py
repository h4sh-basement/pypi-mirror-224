# Generated by Django 3.1.14 on 2022-04-27 14:29

import django.contrib.gis.db.models.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("stores", "0005_auto_20220425_2119"),
    ]

    operations = [
        migrations.AddField(
            model_name="store",
            name="address",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="store",
            name="poly",
            field=django.contrib.gis.db.models.fields.PolygonField(
                blank=True, null=True, srid=4326
            ),
        ),
        migrations.AlterField(
            model_name="store",
            name="location",
            field=django.contrib.gis.db.models.fields.PointField(
                blank=True, null=True, srid=4326
            ),
        ),
        migrations.AlterUniqueTogether(
            name="openinghours",
            unique_together={("weekday", "store")},
        ),
    ]
