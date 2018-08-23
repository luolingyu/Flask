from flask import Blueprint, render_template
from simpledu.models import Course
from simpledu.forms import LoginForm, RegisterForm


#省略url_prefix,默认''/''
front = Blueprint('front', __name__)


@front.route('/')
def index():
    courses = Course.query.all()
    return render_template('index.html', courses=courses)


@front.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html')


@front.route('/register')
def register():
    form = RegisterForm()
    return render_template('register.html')




