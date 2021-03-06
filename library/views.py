from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView, ListView, DeleteView
from rest_framework.generics import ListAPIView

from .models import Book
from .serializers import BookSerializer


# Create your views here.


class BookQuerysetMixin(object):  # created a mixin as i used the same get_queryset method for BookListView and ListAPI
    def get_queryset(self):
        title = self.request.GET.get('title', '')
        author = self.request.GET.get('author', '')
        lang = self.request.GET.get('lang', '')
        after = int(self.request.GET.get('after', '') or 0)
        before = int(self.request.GET.get('before', '') or 9999)
        new_queryset = Book.objects.filter(
            title__icontains=title,
            author__icontains=author,
            lang__icontains=lang,
            pub_date__range=(after, before)
        ).order_by('pk')
        return new_queryset


class BookListView(BookQuerysetMixin, ListView):
    model = Book
    template_name = 'library/book_list.html'
    # paginate_by = 10 ---> pagination is a problem when combined with GET filter attrs TODO: pagination
    context_object_name = 'books'

    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['title'] = self.request.GET.get('title', '')
        context['author'] = self.request.GET.get('author', '')
        context['lang'] = self.request.GET.get('lang', '')
        context['after'] = int(self.request.GET.get('after', '') or 0)
        context['before'] = int(self.request.GET.get('before', '') or 9999)
        return context


class BookAddView(CreateView):
    model = Book
    fields = '__all__'
    template_name = 'library/book_form.html'
    success_url = '/'


class BookEditView(UpdateView):
    model = Book
    fields = '__all__'
    template_name = 'library/book_form.html'
    success_url = '/'


class BookDeleteView(DeleteView):
    model = Book
    success_url = '/'


class GoogleImportView(View):
    def get(self, request):
        return render(request, 'library/google_import.html')

    def post(self, request):  # validation might be a thing to work on in the future TODO: validation
        title = request.POST['title']
        author = request.POST['author']
        pub_date = request.POST['pub_date']
        isbn = request.POST['isbn']
        pages = request.POST['pages']
        cover = request.POST['cover']
        lang = request.POST['lang']
        try:
            Book.objects.create(title=title, author=author, pub_date=pub_date, isbn=isbn, pages=pages, cover=cover,
                                lang=lang)
            return redirect('/')
        except IntegrityError as e:
            return render(request, 'library/google_import.html', {'message': e})


class BookAPIView(BookQuerysetMixin, ListAPIView):
    serializer_class = BookSerializer

#  TODO: fill README, make it look nice
