# Generated by Django 2.0.5 on 2018-07-10 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Mypage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userinfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_username', models.CharField(max_length=40)),
                ('user_name', models.CharField(max_length=40)),
                ('user_sex', models.CharField(max_length=10)),
                ('user_age', models.IntegerField()),
                ('user_grade', models.CharField(max_length=40)),
                ('user_class', models.CharField(max_length=40)),
                ('user_phone', models.CharField(max_length=40)),
                ('user_adress', models.CharField(max_length=200)),
            ],
        ),
        migrations.RemoveField(
            model_name='users',
            name='id',
        ),
        migrations.AlterField(
            model_name='users',
            name='username',
            field=models.CharField(max_length=40, primary_key=True, serialize=False),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='Mypage.Users'),
        ),
    ]
