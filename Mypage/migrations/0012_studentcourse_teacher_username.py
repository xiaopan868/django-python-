# Generated by Django 2.0.5 on 2018-08-02 08:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mypage', '0011_auto_20180731_1914'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentcourse',
            name='teacher_username',
            field=models.CharField(default='', max_length=40),
            preserve_default=False,
        ),
    ]
