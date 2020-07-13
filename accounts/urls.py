from django.urls import path
from django.contrib.auth.views import LoginView

# template_name = 'accounts/login.html'
urlpatterns = [
    path('entrar/', LoginView.as_view(template_name='accounts/login.html'), name='login'),
    #Abaixo adição manual
    # path('novo-usuario/', add_user, name='add_user'),
    # path('login-usuario/', user_login, name='user_login'),
]