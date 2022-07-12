from django.contrib import admin
from django.urls import path,include
from rest_framework.routers import DefaultRouter
from asosiy.view import *

from todo.asosiy.views import TodoView

router = DefaultRouter
router.register('Todo/',TodoView)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
]
