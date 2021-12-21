from django.urls import path
from cart.views import CoursesView
from .views import IndexView
urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('courses', CoursesView.as_view(), name='courses')
]