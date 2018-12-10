# Django
from django import forms
# Project
from .models import Place, PlaceDetails
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class PlaceForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Place
        exclude = ['timestamp']
    
class PlaceDetailForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = PlaceDetails
        exclude = ['timestamp']
