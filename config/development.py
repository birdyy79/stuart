
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'cgrt)p!x^1tggt!wreizgsgj%ab2b+iplry1mq0gp=20$oxbfx'

# The port of the webserver. Defaults to 5000 or the port defined in the
PORT = 5000

DEBUG = True


# 配置 sqlalchemy  "数据库+数据库驱动://数据库用户名:密码@主机地址:端口/数据库?编码"
SQLALCHEMY_DATABASE_URI = "mysql://root:123456@localhost:3306/mycloud"

SQLALCHEMY_TRACK_MODIFICATIONS = True

