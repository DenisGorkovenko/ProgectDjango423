from django.shortcuts import render

from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from users.forms import UserRegisterForm, UserLoginForm, UserUpdateForm


def user_register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            return HttpResponseRedirect(reverse('users:login'))
    return render(request, 'users/register.html', {'form': UserRegisterForm})


def user_login_view(request):
    if request.method == 'POST':
        form = UserLoginForm()
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(email=cd['email'], password=cd['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(reverse('app:index'))  # вместо app имя вашего приложения
                else:
                    return HttpResponse('Аккаунт неактивен!')
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form': form})


@login_required
def user_profile_view(request):
    user_object = request.user
    context = {
        'user_object': user_object,
        'title': f'Ваш профиль {user_object.first_name}',
    }
    return render(request, 'users/profile.html', context)


@login_required
def user_update_view(request):
    user_object = request.user
    if request.method == 'POST':
        form = UserUpdateForm(request.POST, request.FILES, instance=user_object)
        if form.is_valid():
            user_object = form.save()
            user_object.save()
            return HttpResponseRedirect(reverse('users:profile'))
    context = {
        'user_object': user_object,
        'title': f'Изменить профиль {user_object.first_name}',
        'form': UserUpdateForm(instance=user_object)
    }
    return render(request, 'users/update.html', context)


def user_logout_view(request):
    logout(request)
    return redirect('app:index')
