# Generated by Django 3.1.6 on 2021-02-22 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentik_stages_authenticator_webauthn", "0002_default_setup_flow"),
    ]

    operations = [
        migrations.AddField(
            model_name="webauthndevice",
            name="confirmed",
            field=models.BooleanField(
                default=True, help_text="Is this device ready for use?"
            ),
        ),
    ]
