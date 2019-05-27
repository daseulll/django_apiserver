from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer
from rest_framework.exceptions import ValidationError
from .models import Post

class PostSerializer(ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'

    def validate_title(self, title): # 특정필드에만 적용할 경우
        if 'django' not in title:
            raise ValidationError('제목에 django를 꼭 포함시켜 주세요.')
        return title
    
    def validate(self, data):
        if len(data['title']) % 2 == 0 or len(data['content']) % 2 == 0:
            raise ValidationError('글자 개수를 홀수로만 입력해주세요.')
        return data

class UserSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['pk', 'username', 'email']
        