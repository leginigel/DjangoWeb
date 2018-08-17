from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Post
from django.template.defaulttags import register
from django.http import Http404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.

def hello_world(request):
	return render(request, 'ts/hello_world.html', {
		'current_time': str(datetime.now()),
	})

def home(request):
	post_list = Post.objects.all()
	return render(request, 'ts/home.html', {
		'post_list':post_list,
	})
	
def rd_home(request):
	post_list = Post.objects.all()
	return render(request, 'ts/rd_home.html', {
        'post_list':post_list,
	})
	
def training(request):
	from .training_crawler import sw1_data
	
	item_data = tuple(sw1_data.items())
	paginator = Paginator(item_data, 9)
		
	page = request.GET.get('page')
	#item_data = paginator.get_page(page)
	try:
            item_data = paginator.page(page)
	except PageNotAnInteger:
            item_data = paginator.page(1)
	except EmptyPage:
            item_data = paginator.page(paginator.num_pages)
	
	from .training_popular import top, recent
	
	return render(request, 'ts/training.html', {
		'data':item_data,
		'top':top,
		'recent':recent,
	})
	
def training_android(request):
	from .training_crawler import android_data
	
	item_data = tuple(android_data.items())
	paginator = Paginator(item_data, 9)
		
	page = request.GET.get('page')
	#item_data = paginator.get_page(page)
	try:
            item_data = paginator.page(page)
	except PageNotAnInteger:
            item_data = paginator.page(1)
	except EmptyPage:
            item_data = paginator.page(paginator.num_pages)
	
	from .training_popular import top, recent
	
	return render(request, 'ts/training_android.html', {
		'data':item_data,
		'top':top,
		'recent':recent,
	})
	
def training_tv(request):
	from .training_crawler import tv_data
	
	item_data = tuple(tv_data.items())
	paginator = Paginator(item_data, 9)
		
	page = request.GET.get('page')
	#item_data = paginator.get_page(page)
	try:
            item_data = paginator.page(page)
	except PageNotAnInteger:
            item_data = paginator.page(1)
	except EmptyPage:
            item_data = paginator.page(paginator.num_pages)
	
	from .training_popular import top, recent
	
	return render(request, 'ts/training_tv.html', {
		'data':item_data,
		'top':top,
		'recent':recent,
	})
	
def training_other(request):
	from .training_crawler import other_data
	
	item_data = tuple(other_data.items())
	paginator = Paginator(item_data, 9)
		
	page = request.GET.get('page')
	#item_data = paginator.get_page(page)
	try:
            item_data = paginator.page(page)
	except PageNotAnInteger:
            item_data = paginator.page(1)
	except EmptyPage:
            item_data = paginator.page(paginator.num_pages)
	
	from .training_popular import top, recent
	
	return render(request, 'ts/training_other.html', {
		'data':item_data,
		'top':top,
		'recent':recent,
	})
