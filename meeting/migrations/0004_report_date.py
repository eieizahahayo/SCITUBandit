# Generated by Django 2.0.2 on 2018-04-04 09:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('meeting', '0003_auto_20180404_1404'),
    ]

    operations = [
        migrations.AddField(
            model_name='report',
            name='date',
            field=models.DateField(null=True),
        ),
    ]
