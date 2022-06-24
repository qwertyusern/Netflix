
from django.contrib import admin
from django.urls import path
from app1.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('aktyorlar/', AktyorlarApi.as_view()),
    path('aktyor/<int:pk>/', AktyorApi.as_view()),
    path('kinolarlar/', KinolarApi.as_view()),
    path('kino/<int:pk>/', KinoApi.as_view()),
]
