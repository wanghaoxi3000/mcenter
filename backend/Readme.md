# iblog后端
iblog的Django后端，主要通过django-rest-framework搭建。

## 运行
### 安装依赖及初始化数据库
```
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
```

### 运行测试服务器
通过如下命令快速运行一个基于sqlite的测试服务器
```
python manage.py runserver 
```

### 部署
在生产环境部署时，需要设置如下环境变量
- DJANGO_PROD_STATUS=True 

如需使用MySql数据库:
- DJANGO_DB_TYPE=mysql
- MYSQL_INSTANCE_NAME 数据库名
- MYSQL_USERNAME 管理员用户名
- MYSQL_PASSWORD 登陆密码
- MYSQL_PORT_3306_TCP_ADDR 连接地址
- MYSQL_PORT_3306_TCP_PORT 端口号

然后重新运行`python manage.py migrate`初始化数据库
可以通过在一个脚本中使用`export`命令来快速完成这些操作，并在此后启动uwsgi等服务器

### 创建管理员
```
python manage.py createsuperuser
```

### 自定义命令
可通过`python manage.py`执行如下自定义命令 
- initblog

读取此后端项目下的init文件夹下的markdown文件数据，导入数据库。每篇文章将会以init下文件夹名为类别名、文件修改时间为创建时间、未包含在文件夹中的为草稿、以[转载]开头的添加转载属性写入到数据库中

- cleanblog

清空博客数据库
