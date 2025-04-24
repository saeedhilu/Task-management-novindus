from django.urls import path
from .views import *

urlpatterns = [
    path('create/', TaskCreateAPIView.as_view(), name='task-create'),
    # path('tasks/update/<int:pk>/', TaskUpdateAPIView.as_view(), name='task-update'),
]
