from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('products/', views.products, name="products"),
    path('customers/<int:pk_test>/', views.customer, name="customer"),
    path('create_orders/<str:pk>/', views.createOrder, name="create_orders"),
    path('update_orders/<str:pk>/', views.updateOrder, name="update_orders"),
    path('delete_orders/<str:pk>/', views.deleteOrder, name="delete_orders"),
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),
    path('user/', views.userPage, name="user-page"),
    path('account/', views.accountSettings, name="account"),

]
