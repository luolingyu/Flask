# Flask
#
#
#
#
#
#
# 2-1  添加 navbar template/base.html
# 2-2  注册登录页面 
       handers/front.py 添加注册，登录的路由并渲染对应的页面
       template/register(login).html 创建注册，登录页面，在base.html页面将“登录”，“注册”按钮链接到页面
# 2-3  完善数据模型       
      完善user数据模型，首先，在model.py中添加email、_password、role、job字段，
      用户密码为了数据安全存储为原始密码的哈希值，用flask的底层库werkzeug提供了用于生成密码哈希的函数generate_password_hash 和检测密码哈希和密码是否相等的 check_password_hash 函数。
     将 _password 设为一个私有字段，对外暴露的是 password property。用 Python 风格的 setter 在设置 password 时，使用 generate_password_hash 生成并设置哈希密码。接着封装了一个 check_password 函数方法测试用户登录时输入的密码和存储的哈希密码是否相等。然后就是俩个 property 方便判断用户是否是员工或者管理员角色。
# 2-4 使用flask-migrate
     首先，安装：sudo pip3 install flask-migrate
     alembic 是一个数据库版本管理工具，我们在对一个数据表进行添加列，删除列的时候相当于进行了数据库版本的改变。 flask-migrate 是对 almbic 进行的封装，方便我们在 flask 中使用 alembic 管理数据库。
     要使用 flask-migrate 首先要在 create_app 的时候将它注册到 app 上，在 app.py 中,完成后运行 flask db，删除原来的simpledu库，再创建

     初始化
     export FLASK_APP=manage.py
     flask db init
     升级脚本
     flask db migrate -m 'init database'
     将升级写入数据库
     flask db upgrade

# 2-5 创建注册、登录表单
     安装 
     sudo pip3 install flask-wtf
     
     wtforms 是 Python 实现的一个库，它能帮我们在 Python 对象和 HTML form 之间建立一种映射关系，类似于 ORM，方便我们创建表单和在模版中渲染表单。flask-wtf 则是对 wtforms 的封装，方便我们在 flask 中使用 wtforms，并在 wtforms 的基础上添加了 csrf token 的生成和验证机制。
     使用 flask-wtf ，需要在定义的表单类中继承 flask-wtf 提供的 FlaskForm 基类，并为每一个表单输入声明一个字段，代码写在 simpledu/forms.py 中.
     要在 Form 类中为每个输入框声明一个对应的 Field，Field 一般提供俩个参数，第一个是输入框在 html 中的 label，第二个一般是 validators，这里一个列表，里面可以放入多个 wtforms 的验证器，当表单提交时，wtforms 会用列表里的验证器对提交的数据进行验证，对验证失败的数据，wtforms 会将失败信息写入该 Field 下的 errors 列表里面。
Required 验证器表示该字段不能为空，Length 表示值要在提供的俩个界线之间，EqualTo 表示该字段要和另外一个字段值相等。
# 2-6 渲染注册、登录表单
      首先 在front.py中的login和register 函数中将相应的 form 传递到模版中
      然后结合 Bootstrap 的表单样式 分别在 register.html 和 login.html 渲染表单
