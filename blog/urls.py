
from django.urls import path
from blog import views

urlpatterns = [
    # blog/
    path('', views.BlogView.as_view()),
    # path('login/', views.BlogApiView.as_view()),
]
