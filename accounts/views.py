from django.shortcuts import render

# Create your views here.
from django.contrib.auth import login
from django.shortcuts import render, redirect
from accounts.forms import SignupForm


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        print(444)
        if form.is_valid():
            print(333)
            user = form.save()
            login(request, user)
            return redirect('/')
    else:
        form = SignupForm()
        print(2222)
    return render(request, 'accounts/signup.html', {'form': form})