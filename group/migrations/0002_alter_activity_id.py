# Generated by Django 5.0.6 on 2024-06-25 10:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('group', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='id',
            field=models.UUIDField(primary_key=True, serialize=False),
        ),
    ]
