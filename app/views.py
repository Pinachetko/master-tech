from django.shortcuts import render_to_response
from .models import Services, Sections
from django.http import HttpResponse
# Create your views here.


def index(request):
    sections = Sections.objects.all()
    context = []
    for section in sections:
        context.append(
            (section, Services.objects.filter(section=section)))
    return render_to_response("app/index.html", {"context": context[::-1]})


def gen_price(request, section_href):
    price_list = Services.objects.filter(section__href=section_href)
    section = Sections.objects.get(href=section_href)
    return render_to_response("app/price_list.html", {"price_list": price_list, "section_name": section.name})
