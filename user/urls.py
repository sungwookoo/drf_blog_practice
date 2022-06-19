
from django.urls import path
from user import views

urlpatterns = [
    # user/
    path('', views.UserView.as_view()),
    path('login/', views.UserApiView.as_view()),
]
