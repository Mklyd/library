from django.shortcuts import render     
from django.urls import reverse_lazy, reverse

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView


from .models import Book
from .forms import BookForm


class BookListView(ListView):
    model = Book
    template_name = 'book_list.html'
    context_object_name = 'books'


class BookDetailView(DetailView):
    model = Book
    template_name = 'book_detail.html'


class BookCreateView(CreateView):
    model = Book
    form_class = BookForm
    template_name = 'book_form.html'
    success_url = reverse_lazy('book_list')

    def get_success_url(self):
        return reverse('book_detail', args=[str(self.object.id)])
