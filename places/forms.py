# Django
from django import forms
# Project
from .models import Place, PlaceDetails, Products
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin
from ckeditor.fields import RichTextFormField
from ckeditor_uploader.fields import RichTextUploadingField


class PlaceForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Place
        exclude = ['timestamp']

  
    
class PlaceDetailForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    
    class Meta:
        model = PlaceDetails
        exclude = ['timestamp']

    def __init__(self, *args, **kwargs):
        super(PlaceDetailForm, self).__init__(*args, **kwargs)
        self.fields['place'].widget.attrs.update({'class' : 'form-control'})
     

from ckeditor.fields import RichTextFormField


class CkEditorForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = PlaceDetails
        exclude = ['timestamp']

    def __init__(self, *args, **kwargs):
        super(MyForm, self).__init__(*args, **kwargs)
        self.fields['place'].widget.attrs.update({'class' : 'form-control'})

  