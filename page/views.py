from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.
class home(TemplateView):
    template_name = "page\home.html"
def home_1(request):
    return render(request, "page\home.html")
def about(request):
    return render(request, "page\about.html")