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
            "Assigned_Designation",
            "Assigned_Person",
            "Assigned_Range",
            "Assigned_Office",
            "condition",
            "Ownership",
            "description",
            "date_added",
            "get_absolute_url",
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