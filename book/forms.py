# Django
from django import forms
# Project
from tour.models import BookTour
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin


class BookTourForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = BookTour
        exclude = ['timestamp']
    

