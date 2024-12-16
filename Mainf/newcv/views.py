from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.views.generic import View
from .cvforms import CVFORM
from .models import CVINFO
# Create your views here.
#function based views
# def Newcv(request):
#     if request.method == 'POST':
#         form = CVFORM(request.POST)
#         # check validation
#         if form.is_valid():
#             email = form.cleaned_data["email_info"]
#             return HttpResponse(email)
#     else:
#         form = CVFORM()
#     return render(request, "new_cv_form.html", {'form' : form})    

#class based views
class Newcv(View):
    def get(self, request):
        form = CVFORM()
        return render(request, "new_cv_form.html", {'form':form})
    
    def post(self, request):
        form = CVFORM(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email_info"]
            return HttpResponse(email)
    def cvinfor(self, name):
        return Http response(name)


        
