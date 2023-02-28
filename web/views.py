from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from .models import MarkdownFile

import mdtex2html
import urllib.request as get


def index(request):
    # get all possible links
    links = MarkdownFile.objects.order_by("name")
    # render the index page
    template = loader.get_template("web/index.html")
    context = {"links": links}
    # return the links
    return HttpResponse(template.render(context, request))


def render_markdown(request, link):
    # if it exists, render it
    try:
        # get the url from the database
        url = MarkdownFile.objects.get(name=link).link
        # download the file
        file = get.urlopen(url).read().decode()
        # render the file with tables, images, etc
        html = mdtex2html.convert(
            file,
            extensions=[
                "markdown.extensions.extra",
            ],
        )
        # render the file with the template
        template = loader.get_template("web/markdown.html")
        context = {"html": html, "link": link, "url": url}
        # return the rendered file
        return HttpResponse(template.render(context, request))

    except Exception as e:
        # if it doesn't exist, return a 404
        raise Http404("Markdown file not found") from e
