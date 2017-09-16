from django.template import loader
from django.template.response import TemplateResponse
from django.http import HttpResponse
from django.urls import reverse

def home(request):
    pages = [
        'music',
        'code',
        'stories',
        'maelstrom',
    ]
    return TemplateResponse(
            request,
            loader.get_template('index.html'),
            context={'pages': pages}
            )

def music(request):
    return HttpResponse('<h2> M U S I C </h2>')


def code(request):
    return HttpResponse('<h2> C O D E </h2>')

def stories(request):
    return HttpResponse('<h2> S T O R I E S </h2>')

def maelstrom(request):
    return HttpResponse('<h2> M A E L S T R O M </h2>')
