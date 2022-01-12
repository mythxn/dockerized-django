from django import get_version
from django.http import HttpResponse
from django.views.generic import TemplateView
from .tasks import show_hello_world
# Create your views here.


class ShowHelloWorld(TemplateView):
    template_name = 'hello_world.html'

    def get(self, *args, **kwargs):
        show_hello_world.apply()
        return HttpResponse("Hello, World!")