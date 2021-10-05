from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static 

from .forms import LoginForm
from django.contrib.auth import views as auth_view


urlpatterns = [
    # path('', views.home),
    path('', views.ProductView.as_view(), name='home' ),
    path('product-detail/<int:pk>/', views.ProductDetailView.as_view(), name='product-detail'),
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('buy/', views.buy_now, name='buy-now'),
    # path('profile/', views.profile, name='profile'),
    path('profile/', views.ProfileView.as_view(), name='profile'),
    path('address/', views.address, name='address'),
    path('orders/', views.orders, name='orders'),
    path('changepassword/', views.change_password, name='changepassword'),

    path('mobile/', views.mobile, name='mobile'), # /mobiles
    path('mobile/<slug:data>/', views.mobile, name='mobiledata'), #/mobiles/Redmi

    # path('login/', views.login, name='login'),
    # path('registration/', views.customerregistration, name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(
        template_name='app/login.html', 
        authentication_form =LoginForm
        ), name='login'), 
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'), 
    path('logout/', auth_view.LogoutView.as_view(
        next_page='login'
    ), name='logout'),
    path('checkout/', views.checkout, name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'), 
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
