from django.urls import path
from django.conf.urls import include
from actnaturalapp.views import *
from actnaturalapp.models import *


app_name = 'actnaturalapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
    path('logout/', logout_user, name='logout'),
    path('animals/', animal_list, name='animals'),
    path('enrichment_items/', enrichment_item_list, name='enrichment_items'),
    path('enrichment_log_entry/', enrichment_log_entry_list, name='enrichment_log_entries'),
]

