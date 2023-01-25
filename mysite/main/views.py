from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect,HttpResponse
from .forms import UserForm
from .models import UserInfo
from pyuca import Collator
from django.core.mail import send_mail
# Create your views here.
def index(request):
    return HttpResponseRedirect('/home')
def home(request):
    return render(request,'main/home.html',{'request':request})


def regis_form(request):
    if request.method == 'POST':
        print(request.POST)
        fname=request.POST.get('fname')
        lname=request.POST.get('lname')
        marks12=request.POST.get('marks12')
        course=request.POST.get('course')
        mother=request.POST.get('mother')
        father=request.POST.get('father')
        photo=request.FILES.get('photo')
        marksheet=request.FILES.get('marksheet')
        marksheet2=request.FILES.get('marksheet2')
        u=UserInfo(fname=fname,lname=lname,marks12=marks12,course=course,mother=mother,father=father,photo=photo,marksheet=marksheet,marksheet2=marksheet2)
        u.save()
        request.session['form_submitted'] = True
        return redirect('/home') 
    elif 'form_submitted' in request.session:
        # del request.session['form_submitted']   
        request.session['form_submitted'] = True

        return HttpResponse("Form Already Submitted")
    else:
        form = UserForm()
    return render(request,'main/regis_form.html',{"form":form})

def merit(request):
    # c=Collator()
    # u=UserInfo.objects
    # d={}
    # l=[]
    # print(u.all())
    # for entry in u.all():
    #     d[entry.marks12]=entry.id

    # d=sorted(d.items(),reverse=True)
    # for item in d:
    #     l.append(u.get(id=item[1]).fname)
    # print(l)
    # print("lentgh",d.__len__())
    # return render(request,'main/merit.html',{'table':u,'list':l})
    query_set = UserInfo.objects.order_by('marks12').reverse()
    return render(request,'main/merit.html',{'q_set':query_set})

def courses(request):
    return render(request,'main/courses.html',{})

def about(request):
    return render(request,'main/about.html',{})