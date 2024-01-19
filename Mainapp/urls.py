from django.contrib import admin
from django.urls import path

from Mainapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('indexfn',views.indexfn,name="indexfn"),
    path('category',views.category,name="category"),
    path('savecategory',views.savecategory,name="savecategory"),
    path('displaycat',views.displaycat,name="displaycat"),
    path('Admin_login',views.Admin_login,name="Admin_login"),
    path('Add_product',views.Add_product,name="Add_product"),
    path('save_product',views.save_product,name="save_product"),
    path('display_product',views.display_product,name="display_product"),
    path('edit_products/<int:pro_id>/',views.edit_products,name="edit_products"),
    path('adminlogin',views.adminlogin,name="adminlogin"),
    path('admin_logout',views.admin_logout,name="admin_logout")
]