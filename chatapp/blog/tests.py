from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category


class Testing_for_Post_Title(TestCase):
    @classmethod
    def setUp(self):
        test_category = Category.objects.create(name='Cooking')
        test_user_1 = User.objects.create_user(username='testuser1', password='123456789')
        test_post = Post.objects.create(category_id=1, title='testtitle', excerpt='testexcerpt',
                                        content='testcontent', slug='testslug', author_id=1)

    def test_post_title(self):
        post = Post.objects.get(id=1)
        category = Category.objects.get(id=1)
        expected_object_name = f'{post.title}'
        self.assertEqual(expected_object_name, 'testtitle')
        expected_object_excerpt = f'{post.excerpt}'
        self.assertEqual(expected_object_excerpt, 'testexcerpt')
        expected_object_content = f'{post.content}'
        self.assertEqual(expected_object_content, 'testcontent')
        expected_object_slug = f'{post.slug}'
        self.assertEqual(expected_object_slug, 'testslug')
        expected_object_author = f'{post.author}'
        self.assertEqual(expected_object_author, 'testuser1')
        self.assertEqual(str(post), post.title)
        self.assertEqual(str(category), 'Cooking')
