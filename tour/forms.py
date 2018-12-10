from django import forms
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from .models import Tour, PlaceTour, HouseTour, BookTour
from ckeditor.fields import RichTextFormField

class TourForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Tour
        exclude = ['timestamp']
    
class PlaceTourForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = PlaceTour
        exclude = ['timestamp']

class HouseTourForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = HouseTour
        exclude = ['timestamp']

class BookTourForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = BookTour
        exclude = ['timestamp']

class CkEditorForm(forms.Form):
    content = RichTextFormField()