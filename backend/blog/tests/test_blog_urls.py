from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from ..views import IndexView, PostDetailView, PostList


class TestUrl(SimpleTestCase):
    def test_blog_index_url_resolve(self):
        url = reverse('cbv-index')
        self.assertEqual(resolve(url).func.view_class, IndexView)

    def test_blog_detail_url_resolve(self):
        url = reverse('post-detail', kwargs={'pk': 1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView)

    def test_blog_post_list_url_resolve(self):
        url = reverse('post-list')
        self.assertEqual(resolve(url).func.view_class, PostList)

