# Fake views for testing url reverse lookup
from django.http import HttpResponse
from django.template.response import TemplateResponse
from django.template.context import RequestContext
from django.shortcuts import render_to_response


def index(request):
    pass

def client(request, id):
    pass

def client_action(request, id, action):
    pass

def client2(request, tag):
    pass

def template_response_view(request):
    return TemplateResponse(request, 'response.html', {})

def snark(request):
    return HttpResponse('Found him!')

def use_inclusion_tag(request):
    return render_to_response('response_with_incl_tag.html',
                              {},
                              context_instance=RequestContext(request, current_app='advanced'))
