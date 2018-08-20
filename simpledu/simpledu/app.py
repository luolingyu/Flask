from flask import Flask, render_template
from simpledu.config import configs
from simpledu.models import db, Course





def create_app(config):
    """根据传入的config名称，加载不同配置"""
    app = Flask(__name__)
    app.config.from_object(configs.get(config))
    # SQLALchemy 的初始化方式改为使用init_app
    db.init_app(app)
    register_blueprints(app)
    return app


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






