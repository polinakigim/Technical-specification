from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

from electronics_network.models import Network, Product


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class NetworkSerializer(ModelSerializer):

    class Meta:
        model = Network
        exclude = ["created_at"]

    def update(self, instance, validated_data):
        # Убираем debt_to_supplier из данных при обновлении, чтобы поле нельзя было изменить
        validated_data.pop("debt_to_supplier", None)
        return super().update(instance, validated_data)


class NetworkDetailSerializer(ModelSerializer):
    level = serializers.SerializerMethodField()
    products = ProductSerializer(many=True, read_only=True)

    class Meta:
        model = Network
        exclude = ["created_at"]

    def get_level(self, obj):
        if obj.supplier and obj.supplier.id == obj.id:
            return 0

        level = 0
        visited = set()
        current = obj.supplier
        while current and current.id not in visited:
            visited.add(current.id)
            level += 1
            current = current.supplier
        return level
