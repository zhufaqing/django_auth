from django.shortcuts import render,redirect
from .forms import RegisterForm

# Create your views here.
def index(request):
	return render(request,'index.html')


def register(request):
	if request.method == "POST":
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	else:
		form = RegisterForm()
			
	return render(request,'users/register.html',context={'form':form})
