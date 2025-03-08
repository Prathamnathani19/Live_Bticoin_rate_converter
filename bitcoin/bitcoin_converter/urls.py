

from django.contrib import admin
from django.urls import  path
from converter.views import bitcoin_converter

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bitcoin_converter, name='bitcoin_converter'),
]
