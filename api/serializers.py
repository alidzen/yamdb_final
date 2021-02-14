from rest_framework import serializers
from rest_framework.validators import UniqueValidator

from .models import Category, Comment, Genre, Review, Title, User
from .validations import uniq_review


class ObtainCodeSerializer(serializers.Serializer):
    email = serializers.EmailField(
        validators=[UniqueValidator(
            queryset=User.objects.all()
        )]
    )
    username = serializers.CharField(
        max_length=150,
        validators=[UniqueValidator(
            queryset=User.objects.all()
        )]
    )


class ObtainTokenSerializer(serializers.Serializer):
    email = serializers.EmailField()
    confirmation_code = serializers.CharField(max_length=128)


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        fields = ('first_name', 'last_name', 'username', 'bio', 'email', 'role',)
        model = User


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name', 'slug')
        lookup_field = 'slug'


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name', 'slug')
        lookup_field = 'slug'


class TitleViewSerializer(serializers.ModelSerializer):
    genre = GenreSerializer(many=True, read_only=True)
    category = CategorySerializer(read_only=True)
    rating = serializers.FloatField()

    class Meta():
        fields = '__all__'
        model = Title


class TitlePostSerializer(serializers.ModelSerializer):
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug',
    )

    class Meta:
        fields = '__all__'
        model = Title


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    def validate(self, data):
        view = self.context.get('view')
        if view.action == 'create':
            return uniq_review(self.context, data)
        return data

    class Meta:
        exclude = ('title',)
        model = Review


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        slug_field='username',
        read_only=True
    )

    class Meta:
        exclude = ('review',)
        model = Comment
