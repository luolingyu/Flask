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
     alembic 是一个数据库版本管理工具，我们在对一个数据表进行添加列，删除列
的时候相当于进行了数据库版本的改变。 flask-migrate 是对 almbic 进行的封
装，方便我们在 flask 中使用 alembic 管理数据库。
     要使用 flask-migrate 首先要在 create_app 的时候将它注册到 app 上，在 ap
p.py 中,完成后运行 flask db，删除原来的simpledu库，再创建

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
     
     wtforms 是 Python 实现的一个库，它能帮我们在 Python 对象和 HTML form 之
间建立一种映射关系，类似于 ORM，方便我们创建表单和在模版中渲染表单。flask-wtf 
则是对 wtforms 的封装，方便我们在 flask 中使用 wtforms，并在 wtforms 的基础
上添加了 csrf token 的生成和验证机制。
     使用 flask-wtf ，需要在定义的表单类中继承 flask-wtf 提供的 FlaskForm 基
类，并为每一个表单输入声明一个字段，代码写在 simpledu/forms.py 中.
     要在 Form 类中为每个输入框声明一个对应的 Field，Field 一般提供俩个参数
，第一个是输入框在 html 中的 label，第二个一般是 validators，这里一个列表，
里面可以放入多个 wtforms 的验证器，当表单提交时，wtforms 会用列表里的验证器
对提交的数据进行验证，对验证失败的数据，wtforms 会将失败信息写入该 Field 下
的 errors 列表里面。
Required 验证器表示该字段不能为空，Length 表示值要在提供的俩个界线之间，
EqualTo 表示该字段要和另外一个字段值相等。
# 2-6 渲染注册、登录表单
      首先 在front.py中的login和register 函数中将相应的 form 传递到模版中
      然后结合 Bootstrap 的表单样式 分别在 register.html 和 login.html 渲染
表单
# 3-1 使用宏(macro)渲染表单
      1、创建macro.html，存放宏相关代码
      2、注册、登录表单用宏渲染
# 3-2 实现注册功能
      1、在forms.py文件注册表单类RegisterFrom下建立函数根据表单提交的数据创建用户
      2、在front.py中实现注册功能的路由处理函数
         from flask import flash  
         网站需要对用户的一些操作给出成功、失败或者警告等等一些反馈，我们中间调用了 flash 函数，该函数的功能是向模版页面发送一消息，它接收俩个参数，消息的内容和分类，
         frim flask import redirect, url_for
         重定向

# 3-3 自定义表单数据验证器
         在前面的内容中，我们介绍了如何使用 flask-wtf 和 wtforms 创建表单，并使用了 wtforms 提供的一些基本的表单数据验证器，如 Required、Length。wtforms 还提供了一种方式来自定义表单数据验证器。
# 3-4 实现登录功能
         sudo pip3 install flask-login
         登录功能的实现需要借助 flask-login 插件。flask-login 为 Flask 提供了 session 管理的能力，方便开发者实现诸如用户登录、登出、记住用户的 session 等等功能
         继承 UserMixin 主要是为了使用它提供的 is_authenticated 方法判断用户是否是登录状态。
# 3-5 实现退出登录功能
         使用 flask-login 实现退出登录也很简单，只要在用户登录状态下调用 logout_user 函数,在 base.html 中将退出按钮链接到退出路由
         退出登录功能只应该在用户登录的状态下使用，所以这里用 login_required 装饰器保护了这个路由处理函数，如果在未登录状态下访问这个页面会被重定向到登录页面。
# 3-6 表单错误信息显示
         form 对象的每个 field 都有一个 errors 字段，它是一个列表，以自定义表单数据验证器中的 NameField 为例，初始状态下，errors 是一个空列表，表示没有错误信息，但是当 form.validate_on_submit 验证失败时， wtforms 就会将每一个 field 的错误信息添加到它对应的错误列表中：

         ['Length of name can not less than 2']
        现在 form 对象再被传入模版，它的每个 field 的 errors 就不再是空的了。我们要做的就是把每个 field 的错误信息友好的显示出来。

        Bootstrap 已经提供了表单错误显示的样式，我们使用它的样式显示错误信息就可以了，因此需要修改 macros.html 中 render_form 宏里渲染输入框的部分
        我们自定义验证器的错误信息是中文的，而 wtforms 提供的验证器默认的错误信息是英文的。wtforms 提供的每个验证器都可以通过设置 message 参数来修改这一信息。比如修改密码 Length 验证器的默认错误信息可以这样写：

        Length(6, 24, message='密码长度要在6~24个字符之间')
# 3-7 flash消息
        前面的代码中，我们在用户注册成功和退出登录的时候，使用 flash 发送了一条消息，下面我们在模版中显示消息。

        flash 方法不提供分类时，默认的分类是message，这时候在模版中获取消息可以使用：

        get_flashed_messages()
    
    它返回一个消息列表。当要使用自定义的分类时，推荐使用下面的方法迭代消息：
    
{% with messages = get_flashed_messages(with_categories=true) %}
      {% if messages %}
        {% for category, message in messages %}
            {{ message }}
              {% endfor %}
                {% endif %}
{% endwith %}

之前我们使用 flash 时，用的是 success分类，这样是为了结合 Bootstrap 的警告框样式 http://v3.bootcss.com/components/#alerts 。

因为消息每个页面都可能会有，所以把展示消息的代码写在 base.html 中，这样每个页面都能继承它。





























