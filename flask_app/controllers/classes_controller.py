from flask_app import app
from flask import render_template, redirect, request, session
from flask_app.models import user_model, class_model, comment_model

# ALL - CLASSES - DASHBOARD
@app.route("/classes/dashboard")
def classes_all_page():
    if "user_id" in session:
        this_user = user_model.User.get_user_by_id({"user_id": session["user_id"]})
        classes_trainer = class_model.Class.get_all_classes_trainer({"user_id": session["user_id"]})
        classes_scheduled = class_model.Class.get_all_classes_trainee_scheduled({"user_id": session["user_id"]})
        classes_not_scheduled = class_model.Class.get_all_classes_trainee_not_scheduled({"user_id": session["user_id"]})
        return render_template("classes_dashboard.html", user = this_user, classes_trainer = classes_trainer, classes_scheduled = classes_scheduled, classes_not_scheduled = classes_not_scheduled)
    return redirect("/")

# TRAINEE - CLASS - DETAILS
@app.route("/class/details/<int:class_id>")
def class_details_page(class_id):
    if "user_id" in session:  
        all_trainees = class_model.Class.get_all_trainees_class({"class_id": class_id})
        all_comments = comment_model.Comment.get_all_comments_by_class({"class_id": class_id})
        this_class = class_model.Class.get_class_and_trainer_by_id({"class_id": class_id})
        return render_template("class_details.html", all_trainees = all_trainees, all_comments = all_comments, this_class = this_class)
    return redirect("/")

# TRAINEE - CLASS - SCHEDULE
@app.route("/class/schedule/<int:class_id>")
def schedule_class(class_id):
    if "user_id" in session:
        data = {
            "user_id": session["user_id"],
            "class_id": class_id
        }
        class_model.Class.assign_trainee_to_class(data)
        return redirect("/classes/dashboard")
    return redirect("/")

# TRAINEE - CLASS - CANCEL
@app.route("/class/cancel/<int:class_id>")
def cancel_class_trainee(class_id):
    if "user_id" in session:
        data = {
            "user_id": session["user_id"],
            "class_id": class_id
        }
        class_model.Class.trainee_cancel_class(data)
        return redirect("/classes/dashboard")
    return redirect("/")

# TRAINER - CLASS - CREATE
@app.route("/class/new")
def create_class_page():
    if "user_id" in session:
        return render_template("class_create.html")
    return redirect("/")

# TRAINER - CLASS - UPDATE
@app.route("/class/edit/<int:class_id>")
def edit_class_page(class_id):
    if "user_id" in session:  
        this_class = class_model.Class.get_class_and_trainer_by_id({"class_id": class_id})
        return render_template("class_edit.html", this_class = this_class)
    return redirect("/")

# TRAINER - CLASS - CANCEL
@app.route("/class/cancel/<int:class_id>/<int:trainee_id>")
def cancel_class_trainer(class_id, trainee_id):
    if "user_id" in session:
        data = {
            "class_id": class_id,
            "trainee_id": trainee_id
        }
        class_model.Class.trainer_cancel_class(data)
        return redirect(f'/class/trainees/{ class_id }')
    return redirect("/")

# TRAINER - CLASS - DELETE
@app.route("/class/delete/<int:class_id>")
def delete_class(class_id):
    if "user_id" in session:  
        class_model.Class.trainer_delete_class({"class_id": class_id})
        return redirect("/classes/dashboard")
    return redirect("/")

# TRAINER - TRAINEES - VIEW ALL
@app.route("/class/trainees/<int:class_id>")
def view_all_trainees(class_id):
    if "user_id" in session:  
        all_trainees = class_model.Class.get_all_trainees_class({"class_id": class_id})
        this_class = class_model.Class.get_class_by_id({"class_id": class_id})
        all_comments = comment_model.Comment.get_all_comments_by_class({"class_id": class_id})
        return render_template("class_trainees.html", all_trainees = all_trainees, this_class = this_class, all_comments = all_comments)
    return redirect("/")

# TRAINER - CLASS - FORM - CREATE
@app.route("/create_class_form", methods=["POST"])
def create_class_form():
    if "user_id" in session:
        data = {
                "class_name": request.form["class_name"],
                "class_date": request.form["class_date"],
                "class_time": request.form["class_time"],
                "class_location": request.form["class_location"],
                "trainer_id": session["user_id"]
        }
        if class_model.Class.validate_create_class_form(data):
            class_model.Class.trainer_save_class(data)
            return redirect("/classes/dashboard")
        return redirect("/class/new")
    return redirect("/")

# TRAINER - CLASS - FORM - EDIT
@app.route("/edit_class_form/<int:class_id>", methods=["POST"])
def edit_class_form(class_id):
    data = {
            "class_name": request.form["class_name"],
            "class_date": request.form["class_date"],
            "class_time": request.form["class_time"],
            "class_location": request.form["class_location"],
            "class_id": class_id
    }
    if class_model.Class.validate_create_class_form(data):
        class_model.Class.trainer_edit_class(data)
        return redirect("/classes/dashboard")
    return redirect(f'/class/edit/{ class_id }')