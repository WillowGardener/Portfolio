from rest_framework import serializers

from store_app.models import Product, ProductImage, Category

class NestedProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('title','description', 'price', 'productimage_set')

class NestedProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image','alt_text')

class NestedCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('text',)

class ProductSerializer(serializers.ModelSerializer):
    productimageset_detail = NestedProductImageSerializer(read_only=True, source='productimage_set')
    category_set_detail = NestedCategorySerializer(read_only=True, many=True,source='category_set')
    class Meta:
        model = Product
        fields = ('id','title','description','price','category_set', 'productimage_set','productimageset_detail','category_set_detail')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('text','product_set')

class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ('image','alt_text','product')