from rest_framework import serializers

from .models import Category, Product

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= Product
        fields=(
            "id",
            "name",
            "num",
            "registration_num",
            "make",
            "model",
            "Registration_date",
            "Purchased_Price",
            "Current_Valuation",
            "Pool_Assigned",
            "get_absolute_url",
            "description",
            "get_image",
            "get_thumbnail"
        )


class CategorySerializer(serializers.ModelSerializer):
    products=ProductSerializer(many=True)
    class Meta:
        model= Category
        fields=(
            "id",
            "name",
            
            "get_absolute_url",
            "products",
        )