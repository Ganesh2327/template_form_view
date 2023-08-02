from typing import Any, Dict
from django.shortcuts import render
from django.views.generic import TemplateView,FormView
from app.forms import *
from django.http import HttpResponse
# Create your views here.
class tempdatarender(TemplateView):
    template_name='tempdatarender.html'
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context['name']='Ganesh'
        return context
    

class insertdata_temp(TemplateView):
    template_name='insertdata_temp.html'
    def get_context_data(self, **kwargs):
        ECDO=super().get_context_data(**kwargs)
        SFO=studentform
        ECDO['SFO']=SFO
        return ECDO
    def post(self,request):
        SFO=studentform(request.POST)
        if SFO.is_valid():
            SFO.save()
            return HttpResponse('insertdata_temp done') 
        
class formdata(FormView):
    template_name='formdata.html'
    form_class=studentform

    def form_valid(self,form):
        form.save()
        return HttpResponse('formdata is done')
         
       



    
    


