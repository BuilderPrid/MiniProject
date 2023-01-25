from django.shortcuts import render, redirect
from .forms import RegisterForm
from django.core.mail import send_mail

# Create your views here.
def register(response):
    if response.method == "POST":
        form = RegisterForm(response.POST)
        if form.is_valid():
            form.save()
            email = response.POST.get('email')
            send_mail(
                'Welcome to our University',
                'Congratulations on completing the Registration process. We are glad to have you here',
                'smtpPriyanshu@gmail.com',
                ['%s' %email],
                fail_silently=False,
            )
        
        return redirect("/login/")
    else:
        form = RegisterForm()

    return render(response, "register/register.html", {"form":form})