from django.urls import path
from . import views

urlpatterns = [
    path('', views.home , name='home'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register, name='register'),
    path('item/<int:pk>', views.toDoItem, name='itemEdit'),
    path('delete_item/<int:pk>', views.delete_item, name='delete_item'),
    path('add_item/', views.add_item, name='add_item'),
    path('updat_item/<int:pk>', views.update_item, name ="update_item")
    
]
