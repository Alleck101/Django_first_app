from django.shortcuts import render

posts = [
	{
		'author': 'Alleck',
		'title': 'Blog Post 1',
		'content': 'First post here, lads!',
		'date_posted': 'March 19, 2019'
	},
	{
		'author': 'G.Rapefruit',
		'title': 'Blog Post 2',
		'content': 'Second post here, lads!',
		'date_posted': 'March 20, 2019'
	}
]

def home(request):
	context = {
		'posts': posts
	}
	return render(request, 'blog/home.html', context)

	
def about(request):
	return render(request, 'blog/about.html')