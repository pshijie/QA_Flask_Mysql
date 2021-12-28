# 数据库的配置变量
HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = '数据库名'
USERNAME = '用户名'
PASSWORD = '密码'
DB_URI = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI
SECRET_KEY = "Aaudbabdasad"

# 邮箱设置
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_TLS = False
MAIL_USE_SSL = True
MAIL_DEBUG = True
MAIL_USERNAME = "邮箱地址@qq.com"
MAIL_PASSWORD = "邮箱中的授权码"
MAIL_DEFAULT_SENDER = "邮箱地址@qq.com"


