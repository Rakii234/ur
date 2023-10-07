from django.shortcuts import render
from app.forms import *
from django.http import HttpResponse
# Create your views here.
def Registration(request):
    uo=UserForm()
    po=ProfileForm()
    d={'uo':uo,'po':po}
    if request.method=='POST' and request.FILES:
        ud=UserForm(request.POST)
        pd=ProfileForm(request.POST,request.FILES)
        if ud.is_valid() and pd.is_valid():
            nsud=ud.save(commit=False)
            nsud.set_password(ud.cleaned_data['password'])
            nsud.save()

            nspd=pd.save(commit=False)
            nspd.username=nsud
            nspd.save()
            return HttpResponse('Data Inserted')
        else:
            return HttpResponse('Not valid')
    return render(request,'registration.html',d)
