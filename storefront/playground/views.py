from django.contrib.auth import authenticate, login
from django.shortcuts import render, HttpResponse, redirect
from .forms import ContactForm, loginForm, RegisterForm

# Create your views here.
def say_hello(request):
    #print(request.session.get("first_name", "Unknown"))#getter
    #request.session['first_name']
    context = {"title": "hello world!"}
    return render(request, "hello.html", context)


def about_page(request):
    return render(request, "hello.html", {})


def contact_page(request):
    contact_form = ContactForm(request.POST or None)
    context = {
        "title": "Contact",
        "content": "Contact Us",
        "form": contact_form,
    }
    if request.method == "POST":
        print(request.POST.get("fullname"))
        print(request.POST.get("email"))
        print(request.POST.get("content"))
        if contact_form.is_valid():
            print(contact_form.cleaned_data)
    return render(request, "contact/view.html", context)


def login_page(request):
    form = loginForm(request.POST or None)
    print("User logged in")
    context = {"form": form}
    print(request.user.is_authenticated)
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(request, username=username, password=password)
        print(request.user.is_authenticated)
        if user is not None:
            print(request.user.is_authenticated)
            login(request, user)
            context["form"] = loginForm()
            return redirect("/")
        else:
            print("Error")

    return render(request, "auth/login.html", context)


def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {"form": form}

    if form.is_valid():
        print(form.cleaned_data)
    return render(request, "auth/register.html", context)
