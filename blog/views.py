from django.shortcuts import render

posts = [
	{
		'author': 'Pawel',
		'title': 'Blog Post 1',
		'content': 'First post',
		'date_posted': 'May 2019'
	},
	{
		'author': 'Piotr',
		'title': 'Blog Post 2',
		'content': 'Second post',
		'date_posted': 'May 2019'

	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)
	
def about(request):
	return render(request, 'blog/about.html', {'title' : 'About' })


