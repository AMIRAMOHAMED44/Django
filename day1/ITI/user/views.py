from django.contrib.auth import logout
from django.shortcuts import redirect,render
from django.contrib.auth.forms import UserCreationForm
# Create your views here.


def custom_logout(request):
    logout(request)
    return redirect('login')

def register(req):
    context={'form':UserCreationForm()}
    if(req.method=='POST'):
        form=UserCreationForm(data=req.POST)
        if(form.is_bound and form.is_valid()):
            form.save()
            return redirect('login')
        else:
            context['error']=form.errors
    return render(req,'user/register.html',context)
