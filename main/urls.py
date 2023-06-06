from django.urls import path
from .views import IndexView, DetailView, BlogView, OrderCreateView, Detail2View, register

app_name = 'main'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('detail/<int:pk>', DetailView.as_view(), name='detail'),
    path('detail2/<int:pk>', Detail2View.as_view(), name='detail2'),
    path('blog', BlogView.as_view(), name='blog'),
    path('create', OrderCreateView.as_view(), name='create'),
    path('register/', register, name='register'),

]
