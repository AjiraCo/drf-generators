
from rest_framework.serializers import ModelSerializer
from api_v2.models import Post


class PostSerializer(ModelSerializer):

    class Meta:
        model = Post

