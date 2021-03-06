# Generated by Django 2.2 on 2020-02-01 08:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
            ],
        ),
        migrations.CreateModel(
            name='UserInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=64, verbose_name='用户名')),
                ('Password', models.CharField(max_length=64, verbose_name='密码')),
                ('Idnum', models.CharField(max_length=255, verbose_name='身份证号')),
                ('Phone', models.CharField(max_length=255, verbose_name='联系方式')),
                ('Sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=32, verbose_name='性别')),
                ('Realname', models.CharField(max_length=255, verbose_name='姓名')),
                ('Ug_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='iot_bag.UserGroup')),
            ],
            options={
                'verbose_name': '用户信息',
                'verbose_name_plural': '用户信息',
            },
        ),
    ]
