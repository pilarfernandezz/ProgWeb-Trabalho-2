
from django.contrib import admin
from django.urls import include, path
from . import views
from django.contrib.auth.views import LoginView, LogoutView
from django.urls.base import reverse_lazy
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from django.views.generic.edit import UpdateView
from django.contrib.auth.models import User
from django.contrib.auth.views import PasswordResetView
from django.contrib.auth.views import PasswordResetConfirmView
from django.contrib.auth.views import PasswordResetDoneView

urlpatterns = [
    path('arquivos/', include('arquivos.urls')),
    path('accounts/', views.homeSec, name='sec-home'),
    path('accounts/registro/', views.registro, name='sec-registro'),
    path('accounts/login/',
         LoginView.as_view(template_name='registro/login.html'),
         name='sec-login'),
    path('accounts/profile/', views.homeSec, name='sec-home'),
              path('accounts/logout/',
         LogoutView.as_view(next_page=reverse_lazy('sec-home')),
         name='sec-logout'),
    path('accounts/password-change/',
         PasswordChangeView.as_view(template_name='registro/password_change_form.html',
                                    success_url=reverse_lazy('sec-password_change_done')
         ),
         name='sec-password-change'),
    path('accounts/password_change_done',
         PasswordChangeDoneView.as_view(template_name='registro/password_change_done.html'),
         name='sec-password_change_done'
    ),
    path('accounts/updateView/<int:pk>/',
         UpdateView.as_view(
            template_name='registro/user_form.html',
            success_url=reverse_lazy('sec-paginaSecreta'),
            model=User,
            fields=[
                'first_name',
                'last_name',
                'email',
            ]
         ),
         name='sec-updateView'
    ),
    path('accounts/password_reset/',
         PasswordResetView.as_view(
            template_name='registro/password_reset_form.html',
            success_url=reverse_lazy('sec-password_reset_done'),
            from_email='webmaster_do_site@aqui.com.br',
            subject_template_name='registro/password_reset_subject.txt',
            email_template_name='registro/password_reset_email.html',
         ),
         name='sec-password_reset'),
    path('accounts/password_reset_done/',
         PasswordResetDoneView.as_view(
            template_name='registro/password_reset_done.html'
         ),
         name='sec-password_reset_done'
    ),
    path('accounts/password_reset_confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(
            template_name='registro/password_reset_confirm.html',
            success_url=reverse_lazy('sec-password_reset_complete'),
         ),
         name='password_reset_confirm'
    ),
    path('accounts/verificaUsername', views.verificaUsername, name='sec-verificaUsername'),
]