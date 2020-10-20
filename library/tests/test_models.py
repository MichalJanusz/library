from django.test import TestCase

from library.models import Book


class BookModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        Book.objects.create(title='Test Book', author='John Doe', pub_date=1999, isbn=1234567890123, pages=30,
                            lang='en')

    def test_pub_date_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('pub_date').verbose_name
        self.assertEqual(field_label, 'Publication Date')

    def test_isbn_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('isbn').verbose_name
        self.assertEqual(field_label, 'ISBN')

    def test_pages_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('pages').verbose_name
        self.assertEqual(field_label, 'Number of pages')

    def test_cover_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('cover').verbose_name
        self.assertEqual(field_label, 'Link to cover')

    def test_lang_label(self):
        book = Book.objects.get(id=1)
        field_label = book._meta.get_field('lang').verbose_name
        self.assertEqual(field_label, 'Publication language')

    def test_title_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('title').max_length
        self.assertEqual(max_length, 128)

    def test_author_max_length(self):
        book = Book.objects.get(id=1)
        max_length = book._meta.get_field('author').max_length
        self.assertEqual(max_length, 128)

    def test_object_name_is_title(self):
        book = Book.objects.get(id=1)
        expected_name = f'{book.title}'
        self.assertEqual(expected_name, str(book))
