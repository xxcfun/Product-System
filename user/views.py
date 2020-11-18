from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.
from user import models, forms
from user.models import User


def index(request):
    # 首页，重定向到订单页
    if not request.session.get('is_login', None):
        return redirect('login')
    return redirect('order_list')


def bigscreen(request):
    # 大屏
    pass
    return render(request, 'bigscreen.html', {

    })


def login(request):
    if request.session.get('is_login', None):   # 不允许重复登录
        return redirect('index')
    if request.method == 'POST':
        login_form = forms.UserForm(request.POST)
        message = '请输入账号和密码！'
        if login_form.is_valid():
            username = login_form.cleaned_data.get('username')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(name=username)
            except:
                message = '用户不存在！'
                return render(request, 'login.html', locals())    # locals() 函数会以字典类型返回当前位置的全部局部变量
            if user.password == password:
                request.session['is_login'] = True
                request.session['user_id'] = user.id
                request.session['user_name'] = user.name
                request.session['user_power'] = user.power
                return redirect('index')
            else:
                message = '密码不正确！'
                return render(request, 'login.html', locals())
        else:
            return render(request, 'login.html', locals())
    login_form = forms.UserForm()
    return render(request, 'login.html', locals())


def register(request):
    pass
    return render(request, 'register.html')


def logout(request):
    if not request.session.get('is_login', None):
        # 如果本来就没有登录，就不用登出
        return redirect('login')
    request.session.flush()
    return redirect('login')


def mine(request):
    # 个人中心模块
    pk = request.session.get('user_id')
    user = get_object_or_404(User, pk=pk, is_valid=True)
    if request.method == 'POST':
        editpwd = request.POST.get('editpwd')
        checkpwd = request.POST.get('checkpwd')
        if editpwd != checkpwd:
            message = '两次密码不一致'
        else:
            User.objects.filter(pk=pk).update(password=checkpwd)
            message = '修改成功'
    return render(request, 'mine.html', locals())
