from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, "a_home/index.html")
def about(request):
    return render(request, 'a_home/about.html')
def contact(request):
    return render(request, 'a_home/contact.html')
def services(request):
    return render(request, 'a_home/course.html')
def serviceDetails(request):
    return render(request, 'a_home/courseDetails.html')
