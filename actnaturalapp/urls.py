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
    path('animals/<int:animal_id>/change_photo', animal_photo_edit_form, name='animal_photo_edit_form'),

    path('species/<int:species_id>/', animal_list, name='specie'),
    path('species/add_species/', species_form, name='species_form'),
    path('species/<int:species_id>/edit_species', species_edit_form, name="species_edit_form"),

    path('notes/<int:note_id>', animal_note_details, name='note'),
    path('animals/<int:animal_id>/notes/add_note', animal_note_form, name='animal_note_form'),
    path('notes/<int:note_id>/edit_note', animal_note_edit_form, name="animal_note_edit_form"),

    path('enrichment_items/', enrichment_item_list, name='enrichment_items'),
    path('enrichment_items/<int:enrichment_item_id>/', enrichment_item_details, name='enrichment_item'),
    path('enrichment_items/add_enrichment_item/', enrichment_item_form, name='enrichment_item_form'),
    path('enrichment_items/<int:enrichment_item_id>/edit_enrichment_item', enrichment_item_edit_form, name="enrichment_item_edit_form"),
    path('enrichment_items/<int:enrichment_item_id>/change_photo', enrichment_item_photo_edit_form, name='enrichment_item_photo_edit_form'),

    path('enrichment_types/<int:enrichment_type_id>/', enrichment_item_list, name='enrichment_type'),
    path('enrichment_types/add_enrichment_type/', enrichment_type_form, name='enrichment_type_form'),
    path('enrichment_types/<int:enrichment_type_id>/edit_enrichment_type', enrichment_type_edit_form, name="enrichment_type_edit_form"),

    path('animal_enrichment_items/<int:animal_enrichment_item_id>/', animal_enrichment_item_details, name='animal_enrichment_item'),
    path('enrichment_items/<int:enrichment_item_id>/animals/add_approval', animal_enrichment_item_form, name='animal_enrichment_item_form'),

    path('enrichment_log_entries/', enrichment_log_entry_list, name='enrichment_log_entries'),
    path('enrichment_log_entries/<int:enrichment_log_entry_id>/', enrichment_log_entry_list, name='enrichment_log_entry'),

    path('enrichment_log_entries/add_enrichment_log_entry', enrichment_log_entry_form, name="enrichment_log_entry_form"),

    path('enrichment_log_entries/add_enrichment_log_entry/', enrichment_log_entry_details, name="enrichment_log_entry_details"),

    path('enrichment_log_entries/<int:enrichment_log_entry_id>/edit_enrichment_log_entry', enrichment_log_entry_edit_form, name="enrichment_log_entry_edit_form"),
]


