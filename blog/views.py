from django.shortcuts import render

def home_page(request):
	return render(request, 'blog/home_page.html')
# Create your views here.