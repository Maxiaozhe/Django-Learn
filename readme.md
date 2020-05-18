# Django Project 搭建
## 参考资源
1. [Django官网](http://djangoproject.com)
2. [Django Rest Framework](http://www.django-rest-framework.org/tutorial/1-serialization)
## 创建虚拟环境
1. MAC/linux
   ```bash
   python3 -m vent env        #env可以是任何名字，一般我喜欢把它放在工程目录下
   source ./env/bin/activate  #激活虚拟环境(成功后，提示符前会出现:（env）yourUsername$
   deactivate                 #关闭虚拟环境
   ```
2. WIndows
   ```bash
   pip install virtualenv    #安装Virtualenv
   virtualenv env            #生成env路径
   ./env/scripts/activate    #激活虚拟环境(有时Powershell无法执行，需要设置Policy)
   deactivate                #关闭虚拟环境
   ```
   Windows下总是比MAC/linux多一些麻烦，这也是我为什么越来越喜欢在MAC下开发的原因

## 安装Django环境
启动虚拟环境后，我们就可以搭建Django环境了
1. 安装Django: `pip install django`
2. django-admin 的主要命令
   ```bash
   (env)$ django-admin  #列出管理工具的菜单
   ```
   结果
   ```bash
    [django]
        check
        compilemessages
        createcachetable
        dbshell           # dbshell 可以进行数据库操作
        diffsettings
        dumpdata
        flush
        inspectdb
        loaddata
        makemessages
        makemigrations  # 创建/更新数据库Schema
        migrate         # 数据库移植
        runserver       # 启动http server
        sendtestemail
        shell           # python shell
        showmigrations
        sqlflush
        sqlmigrate
        sqlsequencereset
        squashmigrations
        startapp
        startproject    #创建Project
        test
        testserver
        createproject  
   ```
3. 创建Project
   ```bash
   django-admin startproject [YOUR-PROJECT-name]
   ```   
   执行成功后，会在当前目录下创建一个Project目录，并自动生成如下代码
   ```bash
   your-Project
      __init__.py
      __pycache__
      asgi.py
      settings.py
      urls.py
      wsgi.py
   manage.py           # manage.py 调用Django-admin的命令，但只对当前Project起作用
   ```
4. ange.py的功能
```bash
./manage.py help
# 显示结果
[auth]
    changepassword
    createsuperuser

[contenttypes]
    remove_stale_contenttypes

[django]
    check               #检查代码有没有潜在问题
    compilemessages
    createcachetable
    dbshell             #调用DBShell
    diffsettings
    dumpdata
    flush
    inspectdb
    loaddata
    makemessages
    makemigrations
    migrate
    sendtestemail
    shell
    showmigrations
    sqlflush
    sqlmigrate
    sqlsequencereset
    squashmigrations
    startapp
    startproject
    test
    testserver

[sessions]
    clearsessions

[staticfiles]
    collectstatic
    findstatic
    runserver     #启动WebServer
``` 
5. 数据库迁移
   目前还没有写任何代码，但是`Django`自带了了一个开箱即用的管理页面。
   在启动WebServer之前还需要创建数据库，和超级用户。
   ```bash
   cd [YOUR-PROJECT]
   # 自动创建sqlite3数据库
   # 执行后会在当前目录下创建一个db.sqlite3 数据库文件
   ./manage.py migrate
   ```
   看一下生成的数据库结构
   ```bash
   ./manage.py dbshell   #启动数据库sqlite3的dbshell
   sqlite> .tables       #查看生成的数据库表
   ------------------------------------------------
   auth_user_user_permissions
   auth_group                  django_admin_log          
   auth_group_permissions      django_content_type       
   auth_permission             django_migrations         
   auth_user                   django_session            
   auth_user_groups             

   ```
6. 创建超级用户
   ```bash
   ./manage.py createsuperuser
   # 记住输入的用户和密码，后面管理页面要用到
   ```
7. 启动Web Server
   ```bash
   ./manage.py runserver
   -------------------------------------------------
   Django version 3.0.6, using settings 'restapi.settings'
   Starting development server at http://127.0.0.1:8000/
   Quit the server with CONTROL-C.
   ```
   http://127.0.0.1:8000/ 初始网页
   http://127.0.0.1:8000/admin  管理页面 

## 创建自己的APP

1. 添加App
   ```bash
   ./manger.py startapp products
   ```
2. 注册APP
   ```python
   #在settings.py中注册新创建的APP
   INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "products"   #新添加的APP
   ]
   ```
3. 添加Model
   ```python
   # 继承自models.Model，与大多数ORM框架一样可以自动生成数据库映射
   class Product(models.Model):
      productName = models.TextField(default="")
      price = models.FloatField(default=0.0)
      description = models.TextField(default="",blank=True)
      summary = models.TextField()
   ```
4. 数据库迁移
   ```bash
   ./manage.py makemigrations  #创建数据库迁移
   ./manage.py migrate         #数据库迁移
   ```
5. 注册到Admin 页面
   ```python
   #打开 ./admin.py
   #添加以下代码
   from .models import Product
   # Register your models here.
   admin.site.register(Product)
   ```
6. 通过shell操作数据
   ```bash
   ./manage.py shell #启动Python Shell
   ```
   进入Python Shell后，可以直接操作models数据
   ```python
   from products.models import Product
   
   # 取得数据集合
   Product.objects.all() 
   
   # 创建数据
   Product.objects.create(productName='Huawei P20 pro',price=65000)
   Product.objects.create(productName='Huawei P30 pro',price=85000)
   Product.objects.create(productName='Huawei mate30 pro',price=105000)
   
   # 显示
   for prod in Product.objects.all():
       print(f'{prod.id}. {prod.productName} ')

   #取得特定数据
   prod5=Product.objects.get(id=5)
   
   ```
7. [各种字段类型](https://docs.djangoproject.com/zh-hans/3.0/ref/models/fields/)
   
