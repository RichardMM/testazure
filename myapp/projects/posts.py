from .views import projects_mod
from flask import request,session, redirect, url_for, jsonify, flash
from myapp import models, db, files, mail
from flask_mail import Message


def mailer(receipients, msg, sujet):
   msg_obj = Message(subject=sujet, recipients = ['richard.macharia@strathmore.edu'])
   msg_obj.body = msg
   mail.send(msg_obj)
   return "Sent"

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
        issue_det["issue_proj"] = session["project_id"]
        new_details = models.ProjectIssues(**issue_det)
        db.session.add(new_details)
        db.session.commit()
        flash(message="Issue for " + session["project_name"] + " project has been reported")
    return redirect(url_for("projects.project_details",  id=session["project_id"]))

@projects_mod.route('/approveproj/<int:id>', methods=['POST'])
def project_approval(id):
    projects_data = request.form.to_dict()
    projects_data["proj_approval"] = True
    models.Projects.query.filter_by(proj_id=id).update(projects_data)
    db.session.commit()

    # get project manager name and send email also send to approvers
    approver_emails = models.Users.query.with_entities(models.Users.user_email).filter(models.Users.user_approver_rights.is_(True)).all()
    email_list = [addr for addr in approver_emails]
    projects_data = models.Projects.query.filter_by(proj_id=id).first()
    manager_mail = projects_data.manager.query.first().manager_email
    email_list.append(manager_mail)

    #subject body and receipient list
    suj = "Project Approval"
    body = "The project: " + session["project_name"] + " has been approved"
    send_to = list(set(email_list))
    mailer(send_to, body, suj)
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

@projects_mod.route('/ajaxissueanddisb/<int:id>', methods=['POST'])
def issue_and_disb_view(id):
    disbs = models.ProjectDisbursements.query.filter_by(disb_proj=session["project_id"], disb_id=id).first()
    issues = models.ProjectIssues.query.filter_by(issue_proj=session["project_id"], issue_id=id).first()
    if request.form["concern"] == "disb":
        return jsonify({"desc": disbs.disb_desc, "amount":disbs.disb_amt})
    else:

        return jsonify({"title": issues.issue_title, "descr":issues.issue_descr})

@projects_mod.route('/issueresponse', methods=['POST'])
def response_post_ajax():
    issues = models.ProjectIssues.query.filter_by(issue_proj=session["project_id"], issue_id=request.form["id"]).first()
    hold_responses = []
    for row in issues.responses:
        if row.issue_responder==request.form["responder"]:
            hold_responses.append(row.issue_response)
        # responses = row.responses.query.filter_by(issue_responder=).all()
        # for res_row in responses:
        #     hold_responses.append(res_row.issue_response)
    joined_response = "\n".join(hold_responses)
    return jsonify(joined_response)

@projects_mod.route('/saveresponse', methods=['POST'])
def save_iss_response():
    data = request.form.to_dict()
    data["issue_responder"] = session["empcode"]
    res = models.IssueResponse(**data)
    db.session.add(res)
    db.session.commit()
    return jsonify({"status": "ok"})