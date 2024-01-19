from django.urls import path

from frontend import views

urlpatterns = [
    path('home_page',views.home_page,name="home_page"),
    path('product_page',views.product_page,name="product_page"),
    path('about_page',views.about_page,name="about_page"),
    path('servicespage',views.servicespage,name="servicespage"),
    path('Contact_us',views.Contact_us,name="Contact_us"),
    path('save_contact',views.save_contact,name="save_contact"),
    path('login_page',views.login_page,name="login_page"),
    path('signuppage',views.signuppage,name="signuppage"),
    path('save_signup',views.save_signup,name="save_signup"),
    path('cartpage',views.cartpage,name="cartpage"),


]