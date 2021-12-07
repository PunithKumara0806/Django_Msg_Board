from django.test import TestCase
from django.urls import reverse
from .models import Post

'''
Use 'test' as first word or prefix for a function name for executing it as 
a test
'''

class PostModelTest(TestCase):

	def test_txt_content(self):
		post = Post.objects.get(id=1)
		expected_object_name = f'{post.text}'
		self.assertEqual(expected_object_name, 'just a test')
		
	def setUp(self):
		Post.objects.create(text='just a test')

class HomePageViewTest(TestCase):
	
	def setUP(self):
		Post.objects.create(text='this is another test')

	def testview_url_exists_at_proper_location(self):
		resp = self.client.get('/')
		self.assertEqual(resp.status_code, 200)

	def test_view_url_by_name(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)

	def test_view_uses_correct_template(self):
		resp = self.client.get(reverse('home'))
		self.assertEqual(resp.status_code, 200)
		self.assertTemplateUsed(resp, 'home.html')