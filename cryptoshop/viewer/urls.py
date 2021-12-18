from django.urls import path

from .views import IndexView, CoursesView

urlpatterns = [

    path('index', IndexView.as_view(), name='index'),
    path('courses', CoursesView.as_view(), name='courses')
]