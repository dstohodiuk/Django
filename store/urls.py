from django.urls import path
from .import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('', views.index, name='index'),
    path('List of video cards', views.view1, name='view1'),
    path('Information about the video card', views.view2, name='view2'),
    path('Video card brands', views.view3, name='view3'),
    path('Cart', views.view4, name='view4'),
    path('Checkout', views.view5, name='view5'),
    path('product/<int:product_id>/', views.product_detail, name='product_detail'),
    path('category/<int:category_id>/',
         views.category_detail, name='category_detail'),
    path('gpu/<int:gpu_id>/', views.gpu_detail, name='gpu_detail'),
    path('brand/<int:brand_id>/', views.brand_detail, name='brand_detail'),
    path('add-to-cart/<int:gpu_id>/', views.add_to_cart, name='add_to_cart'),
    path('gpus/', views.gpu_list, name='gpu_list'),
    path('checkout/', views.checkout, name='checkout'),
    path('order-success/', views.order_success, name='order_success'),


]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
