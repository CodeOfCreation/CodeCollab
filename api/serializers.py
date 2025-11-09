from rest_framework import serializers
from problems.models import Problem, Solution, Tag
from users.models import CustomUser


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ['id', 'name']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username', 'email']


class ProblemSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    tags = TagSerializer(many=True, read_only=True)
    
    class Meta:
        model = Problem
        fields = ['id', 'title', 'description', 'difficulty', 'language', 'author', 
                  'upvotes', 'views', 'created_at', 'tags', 'test_cases']


class SolutionSerializer(serializers.ModelSerializer):
    author = UserSerializer(read_only=True)
    
    class Meta:
        model = Solution
        fields = ['id', 'problem', 'author', 'code', 'explanation', 'upvotes', 'created_at']