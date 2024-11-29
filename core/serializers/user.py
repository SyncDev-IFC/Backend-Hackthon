from rest_framework.serializers import ModelSerializer, SerializerMethodField
from core.models import User

class UserSerializer(ModelSerializer):
    groups = SerializerMethodField()

    class Meta:
        model = User
        fields = "__all__"
        depth = 1
    
    def get_groups(self, obj):
        return [{"id": group.id, "name": group.name} for group in obj.groups.all()]
