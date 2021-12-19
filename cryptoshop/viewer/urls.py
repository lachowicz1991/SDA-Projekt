from django.urls import path

from .views import IndexView, CoursesView, FaqView, FaqCreateView, FaqUpdateView, FaqDeleteView, FaqDetailView

urlpatterns = [

    path('', IndexView.as_view(), name='index'),
    path('courses', CoursesView.as_view(), name='courses'),
    path('faq', FaqView.as_view(), name='faq'),
    path('faq/new', FaqCreateView.as_view(), name='faq-create'),
    path('faq/<slug:slug>', FaqDetailView.as_view(), name='faq-detail'),
    path('faq/<slug:slug>/edit', FaqUpdateView.as_view(), name='faq-update'),
    path('faq/<slug:slug>/delete', FaqDeleteView.as_view(), name='faq-delete'),
]
