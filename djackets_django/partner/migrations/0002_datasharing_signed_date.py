# Generated by Django 3.2.4 on 2021-07-06 07:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('partner', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='datasharing',
            name='signed_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]