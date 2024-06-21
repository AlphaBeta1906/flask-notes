from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from werkzeug.security import generate_password_hash,check_password_hash
from models import db,User

auth = Blueprint("auth",__name__)

@auth.route("/login",methods=["GET","POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = db.session.execute(db.select(User).filter_by(username=username)).first()[0]
        if user:
            if check_password_hash(user.password,password):
                session["username"] = user.username
                session["id"] = user.id
                session["logged"] = True
                return redirect(url_for("main.index"))
            flash("invalid password",category="danger")
        flash("user not found",category="danger")
    return render_template("login.html",title="login")

@auth.route("/register",methods=["GET","POST"])
def register():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        user = db.session.execute(db.select(User).filter_by(username=username)).first()
        if not user:
            user = User()
            user.username = username
            user.password = generate_password_hash(password)
            db.session.add(user)
            db.session.commit()
            return redirect(url_for("main.index"))
        flash("username has been used",category="danger")
    return render_template("register.html",title="register")

@auth.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("auth.login"))