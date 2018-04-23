from .views import projects_mod
from flask import request
from myapp import models, db, files


@projects_mod.route('/postprojdetails', methods=['POST'])
def upload_projdetails():
    if request.method=='POST':
        proj_data = request.form.to_dict()
        proj_data["proj_approval"] = 0
        new_details = models.Projects(**proj_data)
        db.session.add(new_details)
        db.session.commit()
    return 'ok'

@projects_mod.route('/uploadfile', methods=['POST'])
def upload_files():
    # remember to remove this
    foldername = "photfirst"
    name = request.form["fileName"] + '.'
    uploaded_files = files.save(request.files['projFile'],
                                folder=foldername, name=name)
    return uploaded_files

@projects_mod.route('/postissues', methods=['POST'])
def upload_issues():
    if request.method=='POST':
        items=["issue_title", "issue_descr"]
        issue_det = {item: request.form.get(item) for item in items}
        # remember to remove this
        issue_det["issue_proj"] = 3
        new_details = models.ProjectIssues(**issue_det)
        db.session.add(new_details)
        db.session.commit()
    return 'ok' 



