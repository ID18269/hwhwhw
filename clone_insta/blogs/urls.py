
from django.urls import path
from .views import (BlogCreateView, BlogUpdateView, BlogDeleteView, BlogListView, BlogDetailView,
                    MyBlogsView)

urlpatterns = [
    path('create/', BlogCreateView.as_view(), name='create'),
    path('update/<int:pk>/', BlogUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogDeleteView.as_view(), name='delete'),
    path('list/', BlogListView.as_view(), name='list'),
    path('<int:pk>/', BlogDetailView.as_view(), name='detail'),
    path('myself/', MyBlogsView.as_view(), name='my-blogs'),
]
