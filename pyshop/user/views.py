from django.shortcuts import render, redirect
from .forms import RegisterUserForm, UserUpdateForm, ProfileUpdateForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required


def register(request):
    if request.method == "POST":
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            messages.success(request, f"User created successfully {username}")
            return redirect("login-page")
    else:
        form = RegisterUserForm()

    return render(
        request, "user/register.html", {"title": "Register Page", "form": form}
    )

@login_required
def profile(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST,instance=request.user)
        p_form = ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f"User created Updated")
            return redirect("home-page")
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)
        
    dict = {"title": "Profile Page", "u_form": u_form, "p_form": p_form}
    return render(request, "user/profile.html", dict)

