# Generated by Django 2.0.5 on 2018-07-19 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mypage', '0005_teacherinfo_teacher_teachcourse'),
    ]

    operations = [
        migrations.AlterField(
            model_name='courseinfo',
            name='course_classtime',
            field=models.CharField(max_length=800),
        ),
    ]
