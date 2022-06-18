
from rest_framework import serializers
from ..models import *



class TaskSerializer(serializers.ModelSerializer):
    assigned_to = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all())

    class Meta:
        model = Task
        fields = ('__all__')

    

class TeamSerializer(serializers.ModelSerializer):
    leader = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all()) 

    class Meta:
        model = Team
        fields = ('__all__')



class TeamToMemberSerializer(serializers.ModelSerializer):
    team = serializers.PrimaryKeyRelatedField(queryset=Team.objects.all()) 
    member = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all()) 

    class Meta:
        model = TeamToMember
        fields = ('__all__')


class TaskAssignedToMemberSerializer(serializers.ModelSerializer):
    task = serializers.PrimaryKeyRelatedField(queryset=Task.objects.all()) 
    member = serializers.PrimaryKeyRelatedField(queryset=CustomUser.objects.all()) 

    class Meta:
        model = TaskAssignedToMember
        fields = ('__all__')
