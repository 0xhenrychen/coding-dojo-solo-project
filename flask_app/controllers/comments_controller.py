from flask_app import app
from flask import redirect, request, session
from flask_app.models import comment_model

# USER - COMMENTS - CREATE
@app.route("/create_class_comment_form/<int:class_id>/<which_page>", methods=["POST"])
def comment_form(class_id, which_page):
    if "user_id" in session:
        data = request.form.to_dict()
        data["class_id"] = class_id
        data["user_id"] = session["user_id"]
        comment_model.Comment.save_comment(data)
        if which_page == "details":
            return redirect(f'/class/details/{ class_id }')
        else:
            return redirect(f'/class/trainees/{ class_id }')
    return redirect("/")

# USER - CLASS - DELETE
@app.route("/comment/delete/<int:class_id>/<int:comment_id>")
def delete_comment(class_id, comment_id):
    if "user_id" in session:  
        comment_model.Comment.delete_comment({"comment_id": comment_id})
        return redirect(f'/class/details/{ class_id }')
    return redirect("/")