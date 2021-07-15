from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.CourseListAndCreateAPIView.as_view(), name='courses'),
    path('<int:pk>/', views.CourseDetailUpdateDeleteAPIView.as_view(), name='courses'),
    path('<int:pk>/enroll/',
         views.CourseEnrollAPIView.as_view(), name='enroll'),

]
