from django.test import TestCase
from django.urls import reverse

from library.models import Book
from library.serializers import BookSerializer


class BookListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.bulk_create(
            [Book(title='Test Book', author='John Doe', pub_date=1999, isbn=1234567890123, pages=30, lang='en'),
             Book(title='Książka', author='Adam Kowal', pub_date=1968, isbn=3210987654321, pages=45, lang='pl')]
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/book_list.html')

    def test_view_filtering_is_working(self):
        response = self.client.get(reverse('list') + '?title=Książka&author=Adam+Kowal&lang=pl&after=&before=1969')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.context['books']) == 1)


class BookAddViewTest(TestCase):

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/book/add')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('add'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/book_form.html')


class BookEditViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title='Test Book', author='John Doe', pub_date=1999, isbn=1234567890123,
                                       pages=30,
                                       lang='en')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/book/edit/{self.book.pk}')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('edit', args=[self.book.pk]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('edit', kwargs={'pk': self.book.pk}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/book_form.html')


class GoogleImportViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.book = Book.objects.create(title='Test Book', author='John Doe', pub_date=1999, isbn=1234567890123,
                                       pages=30,
                                       lang='en')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/import/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('import'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('import'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/google_import.html')

    def test_post_success(self):
        response = self.client.post(
            '/import/',
            data={'title': 'Sample Title', 'author': 'John Doe', 'pub_date': '1995', 'isbn': '6273817463123',
                  'pages': '300', 'cover': '', 'lang': 'en'}
        )

        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['Location'], '/')

    def test_post_book_already_exist(self):
        response = self.client.post(
            '/import/',
            data={'title': f'{self.book.title}', 'author': f'{self.book.author}', 'pub_date': f'{self.book.pub_date}',
                  'isbn': f'{self.book.isbn}',
                  'pages': f'{self.book.pages}', 'cover': '', 'lang': f'{self.book.lang}'}
        )

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'Selected book already exists in the database please try again', html=True)


class BookAPIViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.bulk_create(
            [Book(title='Test Book', author='John Doe', pub_date=1999, isbn=1234567890123, pages=30, lang='en'),
             Book(title='Książka', author='Adam Kowal', pub_date=1968, isbn=3210987654321, pages=45, lang='pl')]
        )

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/book/api/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('api'))
        self.assertEqual(response.status_code, 200)

    def test_get_book_data(self):
        response = self.client.get(reverse('api'))
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)

    def test_get_book_data_filtered(self):
        response = self.client.get(reverse('api') + '?title=Książka&author=Adam+Kowal&lang=pl&after=&before=1969')
        books = Book.objects.filter(title__icontains='Książka', author__icontains='Adam Kowal', lang__icontains='pl',
                                    pub_date__range=(0, 1969))
        serializer = BookSerializer(books, many=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, serializer.data)
