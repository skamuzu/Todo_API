from django.urls import path
from . import views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('tasks/', views.task_list, name= 'task_list'),
    path('api/login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('tasks/<int:id>', views.task_item, name='task_item'),
    path('signup/',views.sign_up, name = 'sign_up')
]
