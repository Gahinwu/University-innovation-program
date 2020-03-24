from django.db import models
#用户信息表
class UserInfo(models.Model):
    Ug_id = models.AutoField(primary_key=True,default="")
    Username = models.CharField(max_length=64,verbose_name='用户名')
    Password = models.CharField(max_length=64,verbose_name='密码')
    Idnum = models.CharField(max_length=255,verbose_name='身份证号')
    Phone = models.CharField(max_length=255,verbose_name='联系方式')
    Sex = models.CharField(max_length=32,choices=(('male','男'),('female','女')),default='female',verbose_name='性别')
    Realname = models.CharField(max_length=255,verbose_name='姓名')
    # ug_id 外键
    Ug_id = models.ForeignKey("UserGroup",on_delete=models.CASCADE,null=True)
    
    class Meta:
        verbose_name = '用户信息'
        verbose_name_plural = verbose_name  

class UserGroup(models.Model):
    title = models.CharField(max_length=32,verbose_name='标题')

class Questionnaire(models.Model):
    name = models.CharField(max_length=64,verbose_name='姓名')
    ID_Card = models.CharField(primary_key=True,max_length=255,verbose_name='身份证号')
    SP_Card = models.CharField(max_length=255,verbose_name='社保卡号')
    Age = models.CharField(max_length=32,verbose_name='年龄')
    Sex = models.CharField(max_length=32,choices=(('male','男'),('female','女')),default='female',verbose_name='性别')
    doctors = models.CharField(max_length=32,verbose_name='选择诊治医生')
    symptom1 = models.CharField(max_length=64,verbose_name='症状1')
    symptom2 = models.CharField(max_length=64,verbose_name='症状2')
    symptom3 = models.CharField(max_length=64,verbose_name='症状3')
    symptom4 = models.CharField(max_length=64,verbose_name='症状4')
    symptom5 = models.CharField(max_length=64,verbose_name='症状5')
    symptom6 = models.CharField(max_length=64,verbose_name='症状6')
    symptom7 = models.CharField(max_length=64,verbose_name='症状7')
    other_symptoms = models.CharField(max_length=255,verbose_name='其他症状')
    Ug_id = models.ForeignKey("UserInfo",on_delete=models.CASCADE)

class Databases(models.Model):
    D_id = models.AutoField(primary_key=True,default="")
    Temperature = models.CharField(max_length=8,verbose_name='体温')
    Height = models.CharField(max_length=32,verbose_name='身高')
    Weight = models.CharField(max_length=32,verbose_name='体重')
    BodyFatRate = models.FloatField(max_length=32,verbose_name='体脂率')
    HeartBeatSpo = models.FloatField(max_length=32,verbose_name='心跳血氧')
    ID_Card = models.ForeignKey("Questionnaire",on_delete=models.CASCADE)

        
class MedicalForm(models.Model):
    Med_Result = models.TextField(verbose_name='诊断结果')
    ID_Card = models.ForeignKey("Questionnaire",on_delete=models.CASCADE)

 

