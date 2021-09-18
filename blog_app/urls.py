from django.urls import path

from . import views
from .views import *

urlpatterns = [
    path('<id>', post_detail),
    path('<id>/delete', post_delete),
    path('postCreate', post_create),
    path('postList', post_list),
    path('<id>/update', post_update),
]