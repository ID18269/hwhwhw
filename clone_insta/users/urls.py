
from django.urls import path
from .views import (UserRegisterView, UserLoginView, UserUpdateView, UserDeleteView,
                    UserListView)

urlpatterns = [
    path('register/', UserRegisterView.as_view(), name='register'),
    path('login/', UserLoginView.as_view(), name='login'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', UserDeleteView.as_view(), name='delete'),
    path('list/', UserListView.as_view(), name='list')
]
