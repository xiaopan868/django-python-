# Generated by Django 2.0.5 on 2018-08-01 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mypage', '0013_auto_20180801_1957'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentcourse',
            name='teacher_username',
        ),
        migrations.AlterField(
            model_name='studentcourse',
            name='course_grade',
            field=models.FloatField(),
        ),
    ]
