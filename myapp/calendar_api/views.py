
from datetime import datetime, date
from flask import Blueprint, jsonify, request
from sqlalchemy import and_
from myapp.models import ProjectTasks, Projects
calendar_mod = Blueprint('calendar_api', import_name=__name__)

@calendar_mod.route("/task_dates", methods=["POST", "GET"])
def get_tasks():
    start = datetime.strptime(request.args["start"], "%Y-%m-%d")
    end = datetime.strptime(request.args["end"], "%Y-%m-%d")
    events = []
    tasks = ProjectTasks.query.filter(and_(ProjectTasks.task_start>=start, ProjectTasks.task_start<=end)).all()
    for row in tasks:
        info = {"title": row.task_title,"start":date.strftime(row.task_start, "%Y-%m-%d")}
        events.append(info)
    return jsonify(events)