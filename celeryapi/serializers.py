from rest_framework import serializers
from celeryapi.models import Task

class TaskSerializer(serializers.ModelSerializer):
    """Serializer to map the Talk Model instance into JSON format."""
    task_id = serializers.ReadOnlyField()

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = Task
        fields = ('id', 'name', 'task_id')