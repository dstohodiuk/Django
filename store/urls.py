from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('List of video cards', views.view1, name='view1'),
    path('Information about the video card', views.view2, name='view2'),
    path('Video card brands', views.view3, name='view3'),
    path('Cart', views.view4, name='view4'),
    path('Checkout', views.view5, name='view5'),

]
