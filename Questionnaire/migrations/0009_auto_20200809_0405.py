# Generated by Django 2.0.2 on 2020-08-08 22:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Questionnaire', '0008_auto_20200809_0317'),
    ]

    operations = [
        migrations.AlterField(
            model_name='commonfeaturetable',
            name='timestamp',
            field=models.DateTimeField(),
        ),
    ]
