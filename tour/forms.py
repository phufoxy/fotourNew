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
    
    def __init__(self, *args, **kwargs):
        super(PlaceTourForm, self).__init__(*args, **kwargs)
        self.fields['tour'].widget.attrs.update({'class' : 'form-control'})
        self.fields['name_place'].widget.attrs.update({'class' : 'form-control'})
        self.fields['price'].widget.attrs.update({'class' : 'form-control'})
        self.fields['title'].widget.attrs.update({'class' : 'form-control'})
        self.fields['description'].widget.attrs.update({'class' : 'form-control'})

class HouseTourForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = HouseTour
        exclude = ['timestamp']
    
    def __init__(self, *args, **kwargs):
        super(HouseTourForm, self).__init__(*args, **kwargs)
        self.fields['tour'].widget.attrs.update({'class' : 'form-control'})
        self.fields['name_house'].widget.attrs.update({'class' : 'form-control'})
        self.fields['price'].widget.attrs.update({'class' : 'form-control'})
        self.fields['body'].widget.attrs.update({'class' : 'form-control'})

class BookTourForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = BookTour
        exclude = ['timestamp']

class CkEditorForm(forms.Form):
    content = RichTextFormField()