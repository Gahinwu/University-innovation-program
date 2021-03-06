# Generated by Django 2.2 on 2020-02-26 02:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('iot_bag', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Questionnaire',
            fields=[
                ('name', models.CharField(max_length=64, verbose_name='姓名')),
                ('ID_Card', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='身份证号')),
                ('SP_Card', models.CharField(max_length=255, verbose_name='社保卡号')),
                ('Age', models.CharField(max_length=32, verbose_name='年龄')),
                ('Sex', models.CharField(choices=[('male', '男'), ('female', '女')], default='female', max_length=32, verbose_name='性别')),
                ('doctors', models.CharField(max_length=32, verbose_name='选择诊治医生')),
                ('symptom1', models.CharField(max_length=64, verbose_name='症状1')),
                ('symptom2', models.CharField(max_length=64, verbose_name='症状2')),
                ('symptom3', models.CharField(max_length=64, verbose_name='症状3')),
                ('symptom4', models.CharField(max_length=64, verbose_name='症状4')),
                ('symptom5', models.CharField(max_length=64, verbose_name='症状5')),
                ('symptom6', models.CharField(max_length=64, verbose_name='症状6')),
                ('symptom7', models.CharField(max_length=64, verbose_name='症状7')),
                ('other_symptoms', models.CharField(max_length=255, verbose_name='其他症状')),
                ('username', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot_bag.UserInfo')),
            ],
        ),
        migrations.CreateModel(
            name='Databases',
            fields=[
                ('D_id', models.AutoField(default='', primary_key=True, serialize=False)),
                ('Temperature', models.CharField(max_length=8, verbose_name='体温')),
                ('Height', models.CharField(max_length=32, verbose_name='身高')),
                ('Weight', models.CharField(max_length=32, verbose_name='体重')),
                ('BodyFatRate', models.FloatField(max_length=32, verbose_name='体脂率')),
                ('HeartBeatSpo', models.FloatField(max_length=32, verbose_name='心跳血氧')),
                ('ID_Card', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='iot_bag.Questionnaire')),
            ],
        ),
    ]
