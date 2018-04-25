from .views import projects_mod
from flask import request,session, redirect, url_for, jsonify, flash
from myapp import models, db, files


@projects_mod.route('/postprojdetails', methods=['POST'])
def upload_projdetails():
    if request.method=='POST':
        proj_data = request.form.to_dict()
        new_details = models.Projects(**proj_data)
        db.session.add(new_details)
        db.session.commit()
        flash(message="Project has been saved")
    return redirect(url_for("projects.projects"))

@projects_mod.route('/uploadfile', methods=['POST'])
def upload_files():
    # remember to remove this
    foldername = session["project_name"]
    name = request.form["fileName"] + '.'
    files.save(request.files['projFile'],folder=foldername, name=name)
    flash(message= name + " file for " + session["project_name"] + " project has been saved")
    return redirect(url_for("projects.project_details",  id=session["project_id"]))

@projects_mod.route('/postissues', methods=['POST'])
def upload_issues():
    if request.method=='POST':
        items=["issue_title", "issue_descr"]
        issue_det = {item: request.form.get(item) for item in items}
        # remember to remove this
        issue_det["issue_proj"] = session["project_id"]
        new_details = models.ProjectIssues(**issue_det)
        db.session.add(new_details)
        db.session.commit()
        flash(message="Issue for " + session["project_name"] + " project has been reported")
    return redirect(url_for("projects.project_details",  id=session["project_id"]))

@projects_mod.route('/approveproj/<int:id>', methods=['POST'])
def project_approval(id):
    projects = models.Projects.query.filter_by(proj_id=id).first()
    projects.proj_approval=True
    db.session.commit()
    return jsonify({"status": "ok"})

@projects_mod.route('/savedisbursements/<int:id>', methods=['POST'])
def disb_post(id):
    proj_data = request.form.to_dict()
    proj_data["disb_proj"] = session["project_id"]
    new_details = models.ProjectDisbursements(**proj_data)
    db.session.add(new_details)
    db.session.commit()
    flash(message="Disbursement for " + session["project_name"] + " project has been saved")
    return redirect(url_for("projects.project_details",  id=session["project_id"]))

@projects_mod.route('/savetask/<int:id>', methods=['POST'])
def task_post(id):
    proj_data = request.form.to_dict()
    proj_data["task_proj"] = session["project_id"]
    new_details = models.ProjectTasks(**proj_data)
    db.session.add(new_details)
    db.session.commit()
    flash(message="Task for " + session["project_name"] + " project has been saved")
    return redirect(url_for("projects.project_details",  id=session["project_id"]))