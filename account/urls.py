from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views

app_name = 'account'

urlpatterns = [
    # Login/Logout
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(template_name='account/login.html', next_page='account:dashboard'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # Password change
    path('password-change/',
         auth_views.PasswordChangeView.as_view(
             template_name='registration/password_change_form.html',
             success_url=reverse_lazy('account:password_change_done')
         ),
         name='password_change'),
    path('password-change/done/',
         auth_views.PasswordChangeDoneView.as_view(
             template_name='registration/password_change_done.html'
         ),
         name='password_change_done'),

    # Password reset
    path('password-reset/',
         auth_views.PasswordResetView.as_view(),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(),
         name='password_reset_done'),
    path('password-reset/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(),
         name='password_reset_confirm'),
    path('password-reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(),
         name='password_reset_complete'),

    # Dashboard
    path('', views.dashboard, name='dashboard'),
]



