from rest_framework import serializers
from product.models import ProductModel, CategoryModel, ReviewModel


class CategoryListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = CategoryModel
        fields = 'id name'.split()

class ReviewListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReviewModel
        fields = 'id text rating product'.split()

class ProductReviewSerializer(serializers.ModelSerializer):
    rating_count = serializers.SerializerMethodField()
    class Meta:
        model = ReviewModel
        fields = 'id text rating rating_count'.split()

    def get_rating_count(self, review):
        product = review.product
        all_ratings = ReviewModel.objects.filter(product=product)
        if not all_ratings:
            return 0
        ratings = [r.rating for r in all_ratings if r.rating is not None]
        return sum(ratings) / len(ratings)



class ProductListSerializer(serializers.ModelSerializer):
    category = CategoryListSerializer()
    class Meta:
        model = ProductModel
        fields = 'id title price category'.split()