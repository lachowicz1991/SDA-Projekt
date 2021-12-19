from django.urls import path

from .views import IndexView, CoursesView, FaqView, FaqCreateView

urlpatterns = [

    path('index', IndexView.as_view(), name='index'),
    path('courses', CoursesView.as_view(), name='courses'),
    path('faq', FaqView.as_view(), name='faq'),
    path('faq/new', FaqCreateView.as_view(), name='faq-create'),
]
