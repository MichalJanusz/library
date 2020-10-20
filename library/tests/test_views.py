from django.test import TestCase
from django.urls import reverse

from library.models import Book


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
        Book.objects.create(title='Test Book', author='John Doe', pub_date=1999, isbn=1234567890123, pages=30,
                            lang='en')

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get(f'/book/edit/2')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('edit', args=[2]))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('edit', kwargs={'pk': 2}))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'library/book_form.html')
