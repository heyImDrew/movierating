# Generated by Django 3.2 on 2021-05-09 01:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0005_userprofile_account_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='birth_date',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='email',
            field=models.CharField(blank=True, max_length=255),
        ),
    ]
