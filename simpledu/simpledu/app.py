from flask import Flask, render_template
from simpledu.config import configs
from simpledu.models import db, Course, User
from flask_migrate import Migrate
from flask_login import LoginManager



def create_app(config):
    """根据传入的config名称，加载不同配置"""
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    # SQLALchemy 的初始化方式改为使用init_app
    register_blueprints(app)
    render_extensions(app)
    return app


def render_extensions(app):
    db.init_app(app)
    Migrate(app, db)

    login_manager = LoginManager()
    login_manager.init_app(app)

    @login_manager.user_loader
    def user_loader(id):
        return User.query.get(id)

    login_manager.login_view = 'front.login'


def register_blueprints(app):
    from .handlers import front, course, admin
    app.register_blueprints(front)
    app.register_blueprints(course)
    app.register_blueprints(admin)


    @app.route('/')
    def index():
        courses = Course.query.all()
        return render_template('index.html', courses=courses)


    @app.route('/admin')
    def admin_index():
        return 'admin'






