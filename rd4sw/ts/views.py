from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post

# Create your views here.

def hello_world(request):
	return render(request, 'hello_world.html', {
		'current_time': str(datetime.now()),
	})

def home(request):
	post_list = Post.objects.all()
	return render(request, 'home.html', {
		'post_list':post_list,
	})
	
def rd_home(request):
	post_list = Post.objects.all()
	return render(request, 'rd_home.html', {
        'post_list':post_list,
	})