from django.contrib.contenttypes.models import ContentType

class UserRole:
    """ Defines role of the user """

    USER = "User"
    TEAM_LEADER = "Team Leader"
    TEAM_MEMBER = "Team Member"

    CHOICES = ((USER, "User"), (TEAM_LEADER, "Team Leader"), (TEAM_MEMBER, "Team Member"))



class TaskStatus:
    """ Defines role of the user """

    ASSIGNED = "Assigned"
    IN_PROGRESS = "In Progress"
    UNDER_REVIEW = "Under Review"
    DONE = "Done"

    CHOICES = ((ASSIGNED, ASSIGNED), (IN_PROGRESS, IN_PROGRESS),
                (UNDER_REVIEW, UNDER_REVIEW), (DONE, DONE))



