# Generated by Django 3.2 on 2024-05-15 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Tbl_Employee',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=250)),
                ('email', models.CharField(max_length=250)),
                ('mobile_no', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tbl_employee',
            },
        ),
    ]
