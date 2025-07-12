from django.urls import path
from rest_framework.routers import SimpleRouter

from electronics_network.views import (
    NetworkViewSet,
    ProductListAPIView,
    ProductCreateAPIView,
    ProductRetrieveAPIView,
    ProductDestroyAPIView,
    ProductUpdateAPIView,
)
from electronics_network.apps import ElectronicsNetworkConfig

app_name = ElectronicsNetworkConfig.name

router = SimpleRouter()
router.register("", NetworkViewSet)


urlpatterns = [
    path("products/", ProductListAPIView.as_view(), name="product_list"),
    path("products/create/", ProductCreateAPIView.as_view(), name="product_create"),
    path(
        "products/<int:pk>/", ProductRetrieveAPIView.as_view(), name="product_retrieve"
    ),
    path(
        "products/<int:pk>/delete/",
        ProductDestroyAPIView.as_view(),
        name="product_delete",
    ),
    path(
        "products/<int:pk>/update/",
        ProductUpdateAPIView.as_view(),
        name="product_update",
    ),
]

urlpatterns += router.urls
