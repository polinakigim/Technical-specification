from rest_framework.serializers import ModelSerializer

from electronics_network.models import Network, Product


class NetworkSerializer(ModelSerializer):
    class Meta:
        model = Network
        exclude = ["created_at"]


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"
