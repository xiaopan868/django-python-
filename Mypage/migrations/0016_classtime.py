# Generated by Django 2.0.5 on 2018-08-06 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mypage', '0015_department_college'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classtime',
            fields=[
                ('num', models.CharField(max_length=40, primary_key=True, serialize=False)),
                ('weekday', models.CharField(max_length=20)),
                ('classnum', models.CharField(max_length=20)),
            ],
        ),
    ]
