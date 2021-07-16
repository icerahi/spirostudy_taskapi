from django.urls import path, include
from . import views

urlpatterns = [
    path('instructor/', views.InstructorRegisterAPIView.as_view(),
         name='register_instructor'),
    path('student/', views.StudentRegisterAPIView.as_view(),
         name='register_student'),
]
