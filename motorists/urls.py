from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('register/',views.register, name = 'register_page'),
    path('login/',views.UserLoginView.as_view(), name = 'user_login'),
    path('logout/',views.LogoutView.as_view(), name = 'user_logout'),
    path('profile/', views.show_profile, name='show_profile'),
    path('profile/edit', views.edit_profile, name='edit_profile'),
]
