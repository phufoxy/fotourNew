from django import forms
from .models import House, House_details
from django.forms import CharField, Form, PasswordInput
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class HouseForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = House
        exclude = ['timestamp']

class HouseDetailsForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = House_details
        exclude = ['timestamp']
    
    def __init__(self, *args, **kwargs):
        super(HouseDetailsForm, self).__init__(*args, **kwargs)
        self.fields['house'].widget.attrs.update({'class' : 'form-control'})


