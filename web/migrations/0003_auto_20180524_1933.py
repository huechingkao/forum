# Generated by Django 2.0.5 on 2018-05-24 11:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0002_auto_20180524_1905'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='reply_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
