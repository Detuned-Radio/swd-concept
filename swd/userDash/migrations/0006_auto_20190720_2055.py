# Generated by Django 2.2.1 on 2019-07-20 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('userDash', '0005_auto_20190720_2042'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='address',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
