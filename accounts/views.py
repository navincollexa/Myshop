from django.contrib.auth import(
	authenticate,
	get_user_model,
	login,
	logout,


	)
from django.shortcuts import render

# Create your views here.
def login_view(request):
	title = "login"
	form = UserLoginForm(request.POST or None)
	if form.is_valid()
		username = form.cleaned_data.get("username")
		password = form.cleaned_data.get('password')

	return render(request, "form.html", {"form":form, "title" : title})

def regisered_view(request):
	return render(request, "form.html", {})

def logout_view(request):
	return render(request, "form.html", {})
