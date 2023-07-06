from django.shortcuts import render
from django.views.generic import TemplateView
from .models import Libro

class IndexPageView(TemplateView):
    template_name = 'index.html'

class BookListView(TemplateView):
    template_name = 'book_list.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        books = Libro.objects.all()
        high_rated_books = Libro.objects.filter(valoracion__gt=1500)
        context['books'] = books
        context['high_rated_books'] = high_rated_books
        return context
