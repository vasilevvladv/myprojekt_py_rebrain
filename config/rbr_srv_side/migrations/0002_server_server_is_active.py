# Generated by Django 3.2.12 on 2022-02-25 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbr_srv_side', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='server',
            name='server_is_active',
            field=models.BooleanField(default=False),
        ),
    ]