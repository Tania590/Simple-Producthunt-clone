from django.urls import path
from . import views

urlpatterns = [
    path('create/', views.create_product, name='create'),
    path('detail/<int:pk>/', views.product_detail, name='detail'),
    path('<int:pk>/upvote/', views.upvote, name='upvote'),
]
