from django.urls import path
from .views import CourierViewSet


urlpatterns = [
    path('courier/', CourierViewSet.as_view()),
    path('courier/<int:id>', CourierViewSet.as_view())
]
