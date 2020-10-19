from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import CreateView, UpdateView

from library.models import Book


# Create your views here.

class BookListView(View):
    def get(self, request):
        title = request.GET.get('title', '')
        author = request.GET.get('author', '')
        lang = request.GET.get('lang', '')
        after = int(request.GET.get('after', '') or 0)
        before = int(request.GET.get('before', '') or 9999)
        books = Book.objects.filter(title__icontains=title, author__icontains=author, lang__icontains=lang,
                                    pub_date__range=(after, before)).order_by('pk')
        return render(request, 'library/book_list.html', {'books': books})


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


class GoogleImportView(View):
    def get(self, request):
        return render(request, 'library/google_import.html')

    def post(self, request):  # validation might be a thing to work on in the future
        title = request.POST['title']
        author = request.POST['author']
        pub_date = request.POST['pub_date']
        isbn = request.POST['isbn']
        pages = request.POST['pages']
        cover = request.POST['cover']
        lang = request.POST['lang']
        Book.objects.create(title=title, author=author, pub_date=pub_date, isbn=isbn, pages=pages, cover=cover, lang=lang)
        return redirect('/')
