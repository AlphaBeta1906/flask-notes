from flask import Blueprint,render_template,request,redirect,url_for,flash,session
from models import db,User,Notes
from utils import login_required

main = Blueprint("main",__name__)

@main.route("/")
@login_required
def index():
    notes = db.session.execute(db.select(Notes).filter_by(user_id=session["id"])).all()
    return render_template("index.html",title="index",notes=notes)

@main.route("/create",methods=["GET","POST"])
@login_required
def create():
    if request.method == "POST":
        title = request.form.get("title")
        content = request.form.get("content")
        user_id = session["id"]

        note = Notes()
        note.user_id = user_id
        note.content = content
        note.title = title

        db.session.add(note)
        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("create.html",title="Create new note",edit=False)

@main.route("/<id>",methods=["GET","POST"])
@login_required
def note(id):
    note = db.get_or_404(Notes,id)
    content_title = note.title
    content  = note.content
    if request.method == "POST":
        note.title = request.form.get("title")
        note.content = request.form.get("content")

        db.session.commit()
        return redirect(url_for("main.index"))
    return render_template("create.html",title="Edit note",content_title=content_title,content=content,id=note.id,edit=True)

@main.route("/delete/<id>")
@login_required
def delete(id):
    note = db.get_or_404(Notes,id)
    db.session.delete(note)
    db.session.commit()
    
    return redirect(url_for("main.index"))
