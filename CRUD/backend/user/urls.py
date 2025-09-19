from django.contrib import admin
from django.urls import path
from .views import *

urlpatterns = [

    path('user-list-api', user_list_api.as_view(), name = 'user_list_api'),
    path('add-user', add_user_api.as_view(), name = 'add_user_api'),
    path('get-user-detail/<int:pk>', get_user_detail_api.as_view(), name = 'get_user_detail_api'),
    path('edit-user/<int:pk>', edit_user_api.as_view(), name = 'edit_user_api'),
    path('delete-user/<int:pk>', delete_user_api.as_view(), name = 'delete_user_api'),

]