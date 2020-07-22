from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

#cria-se uma instância do UserCreationForm



class RegisterForm(UserCreationForm):

    #não existe este campo, portanto está sendo criado por aqui e acrescentando aos que já existem
    email = forms.EmailField(label='E-mail')

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exists():
            #se existir exibe um erro
            raise forms.ValidationError('Já existe usuário com este E-mail')
        else:
            #se não existir retorna o email
            return email


    #cria-se um novo save que vai substituir o save do UserCreationForm, colocando o email e salvando.
    def save(self):
        user = super(RegisterForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        user.save()
        return user