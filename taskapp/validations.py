from taskapp.models import *

class TaskValidations:
    def is_user_permitted(user_id, task_id, data):
        user = CustomUser.objects.get(id=user_id)
        task = Task.objects.get(id=task_id)

        if task.assigned_to.leader == user:
            return True
        
        if TaskAssignedToMember.objects.filter(member_id=user_id, task=task).exists():
            unauthorized_fields = ['name', 'started_at', 'completed_at', 'assigned_to']

            for each_field in unauthorized_fields:
                if each_field in data:
                    return False
                    
            return True
            