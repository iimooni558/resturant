"""
URL configuration for ecommerceproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from resturantapp import views as re
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',re.index,name='index'),
    path('details/<int:id>/',re.details,name='details'),
    path('add_to_cart/',re.add_to_cart,name="add_to_cart"),
    path('checkout/',re.checkout,name='checkout'),
    path('auth_login/',re.auth_login,name='auth_login'),
    path('auth_register/',re.auth_register,name='auth_register'),
    path('burger/',re.burger,name='burger'),
    path('side_dishes/',re.side_dishes,name='side_dishes'),
    path('drinks/',re.drinks,name='drinks'),
    path('search/',re.search_products,name='search_products')

]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
