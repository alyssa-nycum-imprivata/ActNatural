from django.urls import path, include
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static
from actnaturalapp.views import *
from actnaturalapp.models import *


app_name = 'actnaturalapp'

urlpatterns = [
    path('', home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', register, name='register'),
    path('logout/', logout_user, name='logout'),

    path('animals/', animal_list, name='animals'),
    path('animals/<int:animal_id>/', animal_details, name='animal'),
    path('animals/add_animal/', animal_form, name='animal_form'),

    path('species/<int:species_id>/', animal_list, name='specie'),
    path('species/add_species/', species_form, name='species_form'),

    path('enrichment_items/', enrichment_item_list, name='enrichment_items'),

    path('enrichment_log_entry/', enrichment_log_entry_list, name='enrichment_log_entries'),
]


