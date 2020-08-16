from django.http import HttpResponse, Http404
from django.template import Template, Context
from django.shortcuts import render
from pathlib import Path
import re


def index(request):
    return render(
        request=request,
        template_name='index.html'
    )


def stagit(request, path):
    HTML_DIR = Path('/home/bar/git/html')
    # HTML_DIR = Path('/home/bar/Documents/Workbench/pybench/barsite/html')

    with open(HTML_DIR.joinpath(path)) as f:
        r = f.read()

    # fix urls
    # p = re.compile(r'<a\s+href\s*=\s*"([^"]+).*')
    # r = re.sub(p, r"""<a href="{% url 'base:stagit' path='\1' %}">\1</a>""", r)
    # print(r)

    c = Context()
    return HttpResponse(
        Template(f'''{{% extends "base.html" %}}
        {{% block content %}}
        {r.split("<body>")[1].split("</body>")[0]}
        {{% endblock %}}
        ''').render(c)
    )
    # return render(
    #     request=request,
    #     template_name='index.html'
    # )
