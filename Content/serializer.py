from .models import Blog
from rest_framework import fields, serializers

class BlogSerializer(serializers.ModelSerializer):

    class Meta:
        model =Blog
        fields='__all__'