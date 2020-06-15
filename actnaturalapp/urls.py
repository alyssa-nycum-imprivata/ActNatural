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
    path('animals/<int:animal_id>/edit_animal', animal_edit_form, name='animal_edit_form'),

    path('species/<int:species_id>/', animal_list, name='specie'),
    path('species/add_species/', species_form, name='species_form'),
    path('species/<int:species_id>/edit_species', species_edit_form, name="species_edit_form"),

    path('notes/<int:animal_id>/', animal_details, name='notes'),
    path('notes/<int:animal_id>/add_note', animal_note_form, name='animal_note_form'),

    path('enrichment_items/', enrichment_item_list, name='enrichment_items'),

    path('enrichment_log_entry/', enrichment_log_entry_list, name='enrichment_log_entries'),
]


