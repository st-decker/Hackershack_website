# Used for template in index func
# from django.http import HttpResponse
# from django.template import loader
# from django.shortcuts import render

# from django.views.generic.base import TemplateView
# from django.contrib.auth.mixins import LoginRequiredMixin


# class ProfileView(LoginRequiredMixin, TemplateView):
#     template_name = 'accounts/profile.html'

# def index(request):
#     print(request.user)
#     return render(request, 'index.html')
#     # Next two lines are the long way of above
#     # template = loader.get_template('index.html')
#     # return HttpResponse(template.render({}, request))

# def about(request):
#     return render(request, 'about.html')

# def contact(request):
#     return render(request, 'contact.html')
