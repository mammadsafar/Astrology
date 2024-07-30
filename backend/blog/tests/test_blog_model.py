# from django.test import TestCase
# from ..models import Post, Category
# from datetime import datetime
# from django.core.files.uploadedfile import SimpleUploadedFile
#
# from django.contrib.auth import get_user_model
# from accounts.models import User, Profile
#
#
# class TestPostModel(TestCase):
#
#     def test_create_post_with_valid_data(self):
#         category_obj = Category.objects.create(name='hello')
#         user = User.objects.create_user(email='test@test.com', password='fasdff3424#@')
#         post = Post.objects.create({
#             "author": user,
#             "image": SimpleUploadedFile('media/image/logo.png', 'file_content', content_type='text/plain'),
#             "title": "Test",
#             "content": "description",
#             "status": True,
#             "category": category_obj,
#             "published_date": datetime.now()
#         })
#
#         self.assertEqual(post.title, 'Test')