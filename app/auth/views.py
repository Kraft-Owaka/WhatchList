from flask import render_template
from . import auth
from flask_login import login_user,logout_user,login_required

@auth.route('/login')
@login_required
def logout():
    logout_user()
    return redirect(url_for("main.index"))

def login():
    return render_template('auth/login.html')