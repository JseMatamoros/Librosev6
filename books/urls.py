from django.urls import path
from .views import IndexPageView, BookListView

urlpatterns = [
    path('', IndexPageView.as_view(), name='index'),
    path('listbook/', BookListView.as_view(), name='listbook'),
]