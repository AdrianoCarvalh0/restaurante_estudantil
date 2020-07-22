from django.conf import settings
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



from .forms import RegisterForm, EditAccountForm

# Create your views here.


@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
    # courses = Course.objects.all()
    # context = {
    #     'courses': courses
    # }
    return render(request, template_name)


def register(request):
    template_name = 'accounts/register.html'
    if request.method == 'POST':
        #cria um formulário passando os dados da requisição
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            #chama o login url que está no settings
            return redirect(settings.LOGIN_URL)
    else:
        #cria um formulário vazio
        form = RegisterForm()
    context = {
        'form': form
    }
    return render(request, template_name, context)

@login_required
def edit_user(request):
    template_name = 'accounts/edit_user.html'
    context = {}
    if request.method == 'POST':
        form = EditAccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            form = EditAccountForm(instance=request.user)
            context['success'] = True
    else:
        form = EditAccountForm(instance=request.user)
    context['form'] = form
    return render(request, template_name, context)



@login_required
def edit_password(request):
    template_name = 'accounts/edit_password.html'
    context = {}
    if request.method == 'POST':
        form = PasswordChangeForm(data=request.POST, user=request.user)
        if form.is_valid():
            form.save()
            context['success'] = True
    else:
        form = PasswordChangeForm(user=request.user)
    context['form'] = form
    return render(request, template_name, context)