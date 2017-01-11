from auth import requires_login
from template_engine.parser import render
from backend.common import *
import db

def signin_handler(request):
    username = request.get_field('username')
    password = request.get_field('password')
    signin = {'username': username, 'password': password}
    request.write(render('signin.html', signin))

def signin_handler_post(request):
    pass

@requires_login
def signout_handler(response):
    response.clear_cookie('current_user')
    response.redirect('/')


def signup_handler(request):
    request.write(render('signup.html', {}))
    ident = request.get_field('id')
    username = request.get_field('username')
    email = request.get_field('email')
    password = request.get_field('password')
    doc = request.get_field('doc')
    gender = request.get_field('gender')
    dob = request.get_field('dob')
    if username != None:
        request.set_secure_cookie("current_user", username)


def signup_handler_post(request):
    ident = request.get_field('id')
    username = request.get_field('username')
    nickname = request.get_field('nickname')
    password = request.get_field('password')
    email = request.get_field('email')
    gender = request.get_field('gender')
    dob = request.get_field('dob')
    profile_pic = request.get_file('profile_picture')
    if profile_pic != (None, None, None):
        filename, content_type, data = profile_pic
        with open(get_upload_path(filename), 'wb') as f:
            f.write(data)
    else:
        print('It failed')
    if username != None:
        request.set_secure_cookie("current_user", username)
    db.User.sign_up(username, password, nickname, email, get_current_time())