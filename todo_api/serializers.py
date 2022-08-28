from rest_framework import serializers
from todo.models import Todos

class TodoListSerializer(serializers.ModelSerializer):
    # user = serializers.ReadOnlyField()
    completed = serializers.ReadOnlyField()
    class Meta:
        model = Todos
        fields = '__all__'

