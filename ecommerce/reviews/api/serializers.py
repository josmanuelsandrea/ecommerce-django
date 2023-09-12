from rest_framework.serializers import ModelSerializer
from reviews.models import Review

class ReviewSerializer(ModelSerializer):
    class Meta:
        model = Review
        fields = ['id', 'user', 'product', 'comment', 'created_at']
        read_only_fields = ['user']

    def create(self, validated_data):
        validated_data['user'] = self.context['request'].user
        review_th = Review.objects.create(**validated_data)
        return review_th