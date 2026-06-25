from rest_framework import serializers
from .models import Category, Cast, Movie, Series

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name']

class CastSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cast
        fields = ['id', 'name', 'role']

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'release_date', 'poster_image', 'categories', 'casts', 'duration_minutes']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        # Display the categories and casts with their str representation during retrieval
        representation['categories'] = [str(category) for category in instance.categories.all()]
        representation['casts'] = [str(cast) for cast in instance.casts.all()]
        return representation

class SeriesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Series
        fields = ['id', 'title', 'description', 'release_date', 'poster_image', 'categories', 'casts', 'seasons_count']

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['categories'] = [str(category) for category in instance.categories.all()]
        representation['casts'] = [str(cast) for cast in instance.casts.all()]
        return representation
