from django.shortcuts import render

# Create your views here.
def blog(request):
    return render(request, 'a_blog/blog.html')

def post(request):
    return render(request, 'a_blog/article_page.html')
