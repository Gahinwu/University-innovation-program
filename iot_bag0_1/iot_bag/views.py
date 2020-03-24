from django.shortcuts import render, redirect, reverse, render_to_response
from django.db import connection
from django.http import HttpResponse, HttpResponseRedirect
from iot_bag import models
from django import forms
from django.contrib.auth.hashers import make_password, check_password
from .models import UserInfo


# 创建存储前端接收信息的表单
class UserForm(forms.Form):
    username = forms.CharField(label="用户名", max_length=255)
    password = forms.CharField(label="密码",max_length=255, widget=forms.PasswordInput())

# create a corsor

# 创建游标
def get_corsor():
    return connection.cursor()



# 注册
def registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    else:
        username = request.POST.get('username')
        password = request.POST.get('password')
        idnum = request.POST.get('idnum')
        phone = request.POST.get('phone')
        realname = request.POST.get('realname')
        sex = request.POST.get('sex')

        cursor = get_corsor()
        cursor.execute("insert into iot_bag_userinfo(username,password,idnum,phone,realname,sex) values('%s','%s','%s','%s','%s','%s')" % (
            username, password, idnum, phone, realname, sex))
        return redirect(reverse('login'))

#注册状态类型：
def RegSuccess(request):
    return render(request, 'reg_statement/RegSuccess.html')

#登录错误类型：
def AnotherError(request):
    return render(request, 'login_statement/AnotherError.html')

def GFormError(request):
    return render(request, 'login_statement/GFormError.html')

def PwdError(request):
    return render(request, 'login_statement/PwdError.html')





# 用户登录

def login(request):
    
    if request.method == 'GET':
        print('method = GET')
        return render(request, 'login.html')

    if request.method == 'POST':
        print('method = POST')
        data = UserForm(request.POST)
        if data.is_valid():
            # 获取表单提交的值
            username = request.POST.get('username')
            password = request.POST.get('password')

            #与数据库的数据进行对比
            use = UserInfo.objects.filter(Username = username, Password = password)    

            if use:
                #将username写入session
                request.session['username'] = username
                response = HttpResponseRedirect('/index/')
                return response

            else:
                response = HttpResponseRedirect('/AnotherError/')
                return response
        else:
            response = HttpResponseRedirect('/GFormError/')
            return response
                




        
# 首页
def index(request):
    username = request.session.get('username')
    if username:
        return render(request, 'index.html',context={'username':username})
    else:
        return HttpResponseRedirect('/AnotherError/')






# 健康调查
def questionnaire(request):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            print('method = GET')
            return render(request, 'questionnaire.html',context={'username':username})   
        
        if request.method =='POST':
            print('method = POST')
            name = request.POST.get('name')
            ID_Card = request.POST.get('ID_Card') 
            SP_Card = request.POST.get('SP_Card')
            Age = request.POST.get('Age')
            Sex = request.POST.get('Sex')
            doctors = request.POST.get('doctors')
            symptom1 = request.POST.get('symptom1')
            symptom2 = request.POST.get('symptom2')
            symptom3 = request.POST.get('symptom3')
            symptom4 = request.POST.get('symptom4')
            symptom5 = request.POST.get('symptom5')
            symptom6 = request.POST.get('symptom6')
            symptom7 = request.POST.get('symptom7')
            other_symptoms = request.POST.get('other_symptoms')
            
            username = request.session.get('username')
            cursor =get_corsor()
            Ug_id = cursor.execute("call find_Ugid('%s')" % username)
            #Ug_id = cursor.execute("select id from iot_bag_userinfo where Username='%s'" % username)            
            cursor.execute("insert into iot_bag_questionnaire(name,ID_Card,SP_Card,Age,Sex,doctors,symptom1,symptom2,symptom3,symptom4,symptom5,symptom6,symptom7,other_symptoms,Ug_id_id) values('%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%d')" 
                % (name,ID_Card,SP_Card,Age,Sex,doctors,symptom1,symptom2,symptom3,symptom4,symptom5,symptom6,symptom7,other_symptoms,Ug_id))
            return redirect(reverse('questionnaire'))
      
    else:
        return HttpResponseRedirect('/AnotherError/')


# 身体健康数据
def bodybase(request):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            username =request.session.get('username')
            cursor =get_corsor()
            Ug_id = cursor.execute("call find_Ugid('%s')" % username)
            cursor.execute("select Realname from iot_bag_userinfo where Username='%s'" % username)
            name = cursor.fetchone()[0]
            cursor.execute("select Sex from iot_bag_userinfo where Username='%s'" % username)
            Sex = cursor.fetchone()[0]
            if Sex == 'man':
                sex = '男'
            elif Sex == 'woman':
                sex = '女'
            else:
                sex =None
            cursor.execute("select Idnum from iot_bag_userinfo where Username='%s'" % username)
            ID_Card = cursor.fetchone()[0]
            cursor.execute("select age from iot_bag_questionnaire where ID_Card='%s'" % ID_Card)
            age = cursor.fetchone()[0]

            #身体检测结果：从数据库获取数据
            cursor.execute("select Temperature from iot_bag_databases where ID_Card_id='%s'" % ID_Card)
            Temperature = cursor.fetchone()[0]
            cursor.execute("select Height from iot_bag_databases where ID_Card_id='%s'" % ID_Card)
            Height = cursor.fetchone()[0]
            cursor.execute("select Weight from iot_bag_databases where ID_Card_id='%s'" % ID_Card)
            Weight = cursor.fetchone()[0]
            cursor.execute("select BodyFatRate from iot_bag_databases where ID_Card_id='%s'" % ID_Card)
            BodyFatRate = cursor.fetchone()[0]
            cursor.execute("select HeartBeatSpo from iot_bag_databases where ID_Card_id='%s'" % ID_Card)
            HeartBeatSpo = cursor.fetchone()[0]

            return render(request,'base.html',
                context={'username':username,'name':name,'sex':sex,'ID_Card':ID_Card,'age':age,
                'Temperature':Temperature,'Height':Height,'Weight':Weight,'BodyFatRate':BodyFatRate,'HeartBeatSpo':HeartBeatSpo})
    # return redirect(reverse())


# 病历单
def MedicalForm(request):
    username = request.session.get('username')
    if username:
        if request.method == 'GET':
            username =request.session.get('username')
            cursor =get_corsor()
            cursor.execute("select Idnum from iot_bag_userinfo where Username='%s'" % username)
            ID_Card = cursor.fetchone()[0]
            cursor.execute("select Med_Result from iot_bag_medicalform where ID_Card_id='%s'" % ID_Card)
            Result = cursor.fetchone()[0]
            return render(request, 'MedicalForm.html',context={'username':username,'Result':Result})
    else:
        return HttpResponseRedirect('/AnotherError/')




# 退出
def logout(request):
    if request.method == 'GET':
        request.session.clear()
        response =HttpResponseRedirect('/login')
        return response




def DigestiveSystem(request):
    username = request.session.get('username')
    if username:
        return render(request, 'form_statement/DigestiveSystem.html')
    else:
        return HttpResponseRedirect('/AnotherError/')