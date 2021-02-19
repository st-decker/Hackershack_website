
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from django.core.mail import send_mail

from stevend_website import settings

from .forms import ContactForm

def contact(request: HttpRequest) -> HttpResponse:
    # Instantiate form, pass it in the context of the request. Will reference later
    if request.method == "GET":
        form = ContactForm()
    elif request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            # extract validated fields from form
            # cleaned_Data is a dictionary that is created when you call validate
            name = form.cleaned_data["name"] # same keys as names (from contact form)
            email = form.cleaned_data["email"]
            message = form.cleaned_data["message"]
            #first arg is subject, second message, third email, fourth is recipient list

            send_mail(
                f'{name} sent an email', message, email, [settings.DEFAULT_FROM_EMAIL]
            )

            # Use new form to clean out the old data and render a success message
            return render(request, "contact.html", {"form": ContactForm(), "success": True})
    else:
        raise NotImplementedError

    return render(request, "contact.html", {"form": form})

# import bleach
# from django.shortcuts import render
# from django.http import HttpRequest, HttpResponse
# from django.core.mail import send_mail

# from stevend_website import settings

# from .forms import ContactForm 

# def contact(request: HttpRequest) -> HttpResponse:
#     # Instantiate form, pass it in the context of the request. Will reference later
#     if request.method == "GET":
#         form = ContactForm()
#     elif request.method == "POST":
#         form = ContactForm(request.POST)
#         if form.is_valid():
#             # extract validated fields from form
#             # cleaned_Data is a dictionary that is created when you call validate
#             name = bleach.clean(form.cleaned_data["name"]) # same keys as names (from contact form)
#             email = bleach.clean(form.cleaned_data["email"])
#             message = bleach.clean(form.cleaned_data["message"])
#             #first arg is subject, second message, third email, fourth is recipient list

#             send_mail(
#                 f'{name} sent an email', message, email, [settings.DEFAULT_FROM_EMAIL]
#             )

#             # Use new form to clean out the old data and render a success message
#             return render(request, "contact.html", {"form": ContactForm(), "success": True})
#     else:
#         raise NotImplementedError

#     return render(request, "contact.html", {"form": form})