from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import ProductModel, CategoryModel, ReviewModel
from product.serializers import CategoryListSerializer, ProductDetailSerializer, ProductListSerializer, ProductReviewSerializer, ReviewListSerializer


@api_view(['GET', 'POST'])
def products_list_api_view(request):
    if request.method == 'GET':
        products = ProductModel.objects.all()
        data = ProductListSerializer(products, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    
    if request.method == 'POST':
        print("пользователь создает продукт:\n" + request.data)
        title = request.data.get("title")
        description = request.data.get("description")
        price = request.data.get("price")
        category_id = request.data.get("category_id")
        rating = request.data.get("rating")

        product = ProductModel.objects.create(
		title=title,
		description=description,
		price=price,
		category_id=category_id
)
        product.rating.set(rating)
        return Response(status=status.HTTP_200_OK, data=ProductDetailSerializer(product).data)


	

@api_view(['GET', 'PUT', 'DELETE'])
def products_detail_api_view(request, product_id):
    try:

        product = ProductModel.objects.get(id=product_id)
    
    except ProductModel.DoesNotExist:

        return Response(data={
            'error': 'product does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        data = ProductListSerializer(product, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        product.title = request.data.get('title')
        product.description = request.data.get('description')
        product.price = request.data.get('price')
        product.category_id = request.data.get('category_id') # type: ignore
        product.rating.set(request.data.get('rating'))
        product.save()
        return Response(status=status.HTTP_201_CREATED, data=ProductDetailSerializer(product).data)
    if request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def categories_list_api_view(request):
    if request.method == 'GET':
        categories = CategoryModel.objects.all()
        data = CategoryListSerializer(categories, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        print(f"пользователь создает категорию:\n {request.data}")
        name = request.data.get("name")
        category = CategoryModel.objects.create(
            name=name
        )
        return Response(status=status.HTTP_201_CREATED, data=CategoryListSerializer(category, many=False).data)
    




@api_view(['GET', 'PUT', 'DELETE'])
def categories_detail_api_view(request, category_id):
    try:
        category = CategoryModel.objects.get(id=category_id)
    except CategoryModel.DoesNotExist:
        return Response(data={
            'error': 'category does mot exist'
        }, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = CategoryListSerializer(category, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        category.name = request.data.get('name')
        category.save()
        return Response(status=status.HTTP_201_CREATED, data=CategoryListSerializer(category, many=False).data)
    if request.method == 'DELETE':
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'POST'])
def reviews_list_api_view(request, product_id=None):
    if product_id is None:
        if request.method == 'GET':
            reviews = ReviewModel.objects.all()
            data = ReviewListSerializer(reviews, many=True).data
            return Response(data=data, status=status.HTTP_200_OK)
        if request.method == 'POST':
            return Response(status=status.HTTP_400_BAD_REQUEST,
                            data={
                                "error": "You can't create a review without a product."
                            })
    
    if request.method == 'GET':
        reviews = ReviewModel.objects.filter(product__id=product_id)
        data = ProductReviewSerializer(reviews, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'POST':
        text = request.data.get('text')
        rating = request.data.get('rating')
        review = ReviewModel.objects.create(
            text=text,
            rating=rating,
            product_id=product_id
        )
        return Response(status=status.HTTP_201_CREATED, data=ReviewListSerializer(review, many=False).data)


@api_view(['GET', 'PUT', 'DELETE'])
def reviews_detail_api_view(request, review_id):
    try:
        review = ReviewModel.objects.get(id=review_id)
    except ReviewModel.DoesNotExist:
        return Response(data={
            'error': 'review does mot exist'
        }, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        data = ReviewListSerializer(review, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    if request.method == 'PUT':
        review.text = request.data.get('text')
        review.rating = request.data.get('rating')
        review.product_id = request.data.get('product_id') # type: ignore
        review.save()
        return Response(status=status.HTTP_201_CREATED, data=ReviewListSerializer(review, many=False).data)
    if request.method == 'DELETE':
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)