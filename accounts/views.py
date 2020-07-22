from django.conf import settings
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required



from .forms import RegisterForm

# Create your views here.



@login_required
def dashboard(request):
    template_name = 'accounts/dashboard.html'
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