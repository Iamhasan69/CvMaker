from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from .cvforms import CVFORM
from .models import CVINFO
# Create your views here.
def Newcv(request):
    if request.method == 'POST':
        form = CVFORM(request.POST)
        # check validation
        if form.is_valid():
            skills = form.cleaned_data["email_info"]

            return HttpResponse(skills)
    else:
        form = CVFORM()
    return render(request, "new_cv_form.html", {'form' : form})    



        
