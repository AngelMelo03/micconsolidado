# Generated by Django 3.2.8 on 2021-12-01 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Consolidado',
            fields=[
                ('ciudad', models.CharField(max_length=255, null=True)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('total_ventas', models.FloatField(null=True)),
            ],
        ),
    ]
