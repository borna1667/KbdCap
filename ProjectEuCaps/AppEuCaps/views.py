from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

def landing_page(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        # TODO: Save the email to your database or mailing list
        return HttpResponseRedirect(reverse('landing_page'))
    return render(request, 'landing_page.html')
