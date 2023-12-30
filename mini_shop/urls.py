from django.urls import path
from . import views


urlpatterns = [
    path('order-minishop/', views.order_minishop, name='order_minishop')
]


 
 