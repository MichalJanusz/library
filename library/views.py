from django.shortcuts import render
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
                                    pub_date__range=(after, before))
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
