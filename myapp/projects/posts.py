from .views import projects_mod
from flask import request
from myapp import models, db, files


@projects_mod.route('/postprojdetails', methods=['POST'])
def projdetails():
    if request.method=='POST':
        proj_data = request.form.to_dict()
        proj_data["proj_approval"] = 0
        new_details = models.Projects(**proj_data)
        db.session.add(new_details)
        db.session.commit()
    return 'ok'

@projects_mod.route('/uploadfile', methods=['POST'])
def upload_files():
    foldername = "photfirst"
    name = request.form["fileName"] + '.'
    uploaded_files = files.save(request.files['projFile'],
                                folder=foldername, name=name)
    return uploaded_files


