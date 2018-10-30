
from django.contrib import admin
from django.urls import path

from name.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('insert', insert),

]
