from django.urls import path, include
from . import views
from .views import signup, MyLoginView
from django.contrib.auth.views import LoginView, LogoutView

urlpatterns = [
    path('', views.home, name = 'home'),
    path('create/', views.create, name = 'create'),
    path('detail/<int:credit_id>', views.detail, name = 'detail'),
    path('delete/<int:credit_id>', views.delete, name = 'delete'),
    path('update/<int:credit_id>', views.update, name = 'update'),
    path('signup/', signup, name="signup"),
    path('login/', MyLoginView.as_view(), name="login"),
    path('logout/', LogoutView.as_view(), name="logout"),
]
