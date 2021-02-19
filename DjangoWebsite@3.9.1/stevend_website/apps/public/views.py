# Used for template in index func
# from django.http import HttpResponse
# from django.template import loader
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse

# from django.views.generic.base import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin

# def index(request):
#     print(request.user)
#     return render(request, 'index.html')
#     # Next two lines are the long way of above
#     # template = loader.get_template('index.html')
#     # return HttpResponse(template.render({}, request))


def index(request: HttpRequest) -> HttpResponse:
    return render(request, "index.html")


def about(request: HttpRequest) -> HttpResponse:
    return render(request, "about.html")


# def contact(request: HttpRequest) -> HttpResponse:
#     return render(request, "contact.html")
