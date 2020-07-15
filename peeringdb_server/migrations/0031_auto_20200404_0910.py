# Generated by Django 2.2.9 on 2020-04-04 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("peeringdb_server", "0030_affiliation_request_status_add_canceled"),
    ]

    operations = [
        migrations.AlterField(
            model_name="network",
            name="info_never_via_route_servers",
            field=models.BooleanField(
                default=False,
                help_text="Indicates if this network will announce its routes via route servers or not",
            ),
        ),
    ]
