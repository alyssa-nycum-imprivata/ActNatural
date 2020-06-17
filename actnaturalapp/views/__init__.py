from .home import home
from .auth.logout import logout_user
from .auth.register import register

from .animals.animal_list import animal_list
from .animals.animal_details import animal_details
from .animals.animal_form import animal_form, animal_edit_form, animal_photo_edit_form

from .species.species_form import species_form, species_edit_form

from .notes.animal_note_details import animal_note_details
from .notes.animal_note_form import animal_note_form, animal_note_edit_form

from .enrichment_items.enrichment_item_list import enrichment_item_list
from .enrichment_items.enrichment_item_details import enrichment_item_details
from .enrichment_items.enrichment_item_form import enrichment_item_form

from .enrichment_types.enrichment_type_form import enrichment_type_form

from .enrichment_log_entries.enrichment_log_entry_list import enrichment_log_entry_list

