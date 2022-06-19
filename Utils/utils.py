from taskapp.models import *
from taskapp.task import send_mail_task


def send_task_creation_notification(task_id):
    task = Task.objects.get(id=task_id)
    team_leader = task.assigned_to.leader
    email = team_leader.email
    subject = "Task assigned update"
    body = f"""
              Hello,
              Task - {task_id} is assigned to Team - {task.assigned_to.name}
              on {str(task.started_at).split('+')[0]}
            """
    # call celery task to send email
    send_mail_task.delay([email], subject, body)


def add_team_members(member_ids, team_id):
    if not member_ids:
        return

    members = member_ids.split(',')
    for each_member in members:
        obj, created = TeamToMember.objects.get_or_create(member_id=each_member, team_id=team_id)
        
    


    


