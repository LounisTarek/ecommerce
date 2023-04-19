from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('category/<str:slug>', views.Category, name="category"),
    path('productview/<int:pk>', views.productdetail, name="productview"),
    path('register', views.register, name="register"),
    path('login', views.signin, name="login"),
    path('logout', views.signout, name="logout"),
    path('add-to-cart', views.addtocart, name="addtocart"),
    path('cart', views.viewcart, name="cart"),
    path('deletecart/<int:pk>', views.deletecart, name="deletecart"),
    path('addtowishlist<int:pk>', views.addtowishlist, name="addtowishlist"),
    path('viewwishlist', views.viewwishlist, name="viewwishlist"),
    path('search', views.search, name="search"),

]