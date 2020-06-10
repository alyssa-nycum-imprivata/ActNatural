from django.urls import path
from django.conf.urls import include
from actnaturalapp.views import *
from actnaturalapp.models import *


app_name = 'actnaturalapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('logout/', logout_user, name='logout'),
]