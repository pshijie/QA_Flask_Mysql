# 功能介绍
> - 用户登录/注册/退出
> - 发布问答
> - 发表评论
> - 关键字搜索

# 运行代码
> 1. 安装环境:
     `pip install -r requirement.txt`
> 2. 修改配置: 
     修改config.py中数据库信息以及QQ邮箱的信息
> 3. 生成数据库:
     `flask db init`
     > `flask db migrate`
     > `flask db upgrade`
> 4. 执行项目:`python app.py` 