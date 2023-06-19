from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "Home.html"
    
class NoPageView(TemplateView):
    template_name = "No.html"