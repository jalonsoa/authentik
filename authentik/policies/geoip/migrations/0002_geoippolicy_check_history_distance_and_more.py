# Generated by Django 5.0.10 on 2025-01-02 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_policies_geoip", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="geoippolicy",
            name="check_history_distance",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="geoippolicy",
            name="check_impossible_travel",
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name="geoippolicy",
            name="distance_tolerance_km",
            field=models.PositiveIntegerField(default=50),
        ),
        migrations.AddField(
            model_name="geoippolicy",
            name="history_login_count",
            field=models.PositiveIntegerField(default=5),
        ),
        migrations.AddField(
            model_name="geoippolicy",
            name="history_max_distance_km",
            field=models.PositiveBigIntegerField(default=100),
        ),
        migrations.AddField(
            model_name="geoippolicy",
            name="impossible_tolerance_km",
            field=models.PositiveIntegerField(default=100),
        ),
    ]
