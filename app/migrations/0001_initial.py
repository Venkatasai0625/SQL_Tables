# Generated by Django 5.0.3 on 2024-04-22 10:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DEPT',
            fields=[
                ('DEPTNO', models.IntegerField(primary_key=True, serialize=False)),
                ('DNAME', models.CharField(max_length=100)),
                ('LOC', models.CharField(max_length=99)),
            ],
        ),
    ]