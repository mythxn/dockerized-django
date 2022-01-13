from django.http import HttpResponse
from django.views import View

from .tasks import show_hello_world


class ShowHelloWorld(View):

    def get(self, *args, **kwargs):
        show_hello_world.apply()
        return HttpResponse("Hello, World!")
