from rest_framework import serializers
from .models import *

class TodoSer(serializers.ModelSerializer):
    class Meta:
        models = Todo
        filter = "__all__"