from django.shortcuts import render, redirect
from .forms import CustomUserForm, UserForm
from django.http import HttpResponse

def register_user(request):
    if request.method == 'POST':
        custom_user_form = CustomUserForm(request.POST)
        user_form = UserForm(request.POST, request.FILES)

        if custom_user_form.is_valid() and user_form.is_valid():
         
            custom_user = custom_user_form.save()
           
            user = user_form.save(commit=False)  
            user.user_id = custom_user  
            user.save()
            return HttpResponse("success")

    else:
        custom_user_form = CustomUserForm()
        user_form = UserForm()

    return render(request, 'register.html', {'custom_user_form': custom_user_form, 'user_form': user_form})
