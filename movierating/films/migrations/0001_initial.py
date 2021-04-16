# Generated by Django 3.2 on 2021-04-16 00:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('custominformation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='films.custominformation')),
            ],
            bases=('films.custominformation',),
        ),
        migrations.CreateModel(
            name='Series',
            fields=[
                ('custominformation_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='films.custominformation')),
            ],
            bases=('films.custominformation',),
        ),
    ]
