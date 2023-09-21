from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

# Create your views here.
def register(request):
    if request.method == 'POST':
        form= UserCreationForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data.get('username')
            messages.success(request,'Welcome {},Your Account has been succesfully created'.format(username))
            
            form.save()
            return redirect('food:index')
        
    else:
        form = UserCreationForm()
        context = {
            'form':form
        }
    

        return render(request,'users/register.html', context)