from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('Список відеокарт/', views.view1, name='view1'),
    path(' Інформація про відеокарту/', views.view2, name='view2'),
    path('Бренди відеокарт/', views.view3, name='view3'),
    path('Корзина/', views.view4, name='view4'),
    path('Оформлення замовлення/', views.view5, name='view5'),
]
