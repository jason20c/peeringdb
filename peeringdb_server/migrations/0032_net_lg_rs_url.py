# Generated by Django 2.2.9 on 2020-04-04 09:11

from django.db import migrations
import django_peeringdb.models.abstract


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0031_auto_20200404_0910"),
    ]

    operations = [
        migrations.AlterField(
            model_name="network",
            name="looking_glass",
            field=django_peeringdb.models.abstract.LG_URLField(
                blank=True, max_length=255
            ),
        ),
        migrations.AlterField(
            model_name="network",
            name="route_server",
            field=django_peeringdb.models.abstract.LG_URLField(
                blank=True, max_length=255
            ),
        ),
    ]
