from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

# Create your views here.
from .forms import LoginForm


def login_view(request, *args, **kwargs):
    form = LoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(request, username=username, password=password)
        if user is None:
            # attempt = request.session.get('attempt') or 0
            # request.session['attempt'] = attempt + 1
            # return redirect("/invalid-password")
            request.session['invalid_user'] = 1
            return render(request, "forms.html", {"form": form})
        login(request, user)
        return redirect("/")
    return render(request, "forms.html", {"form": form})
