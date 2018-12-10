from django import forms
from .models import Tourer, Account
from django.forms import CharField, Form, PasswordInput
from bootstrap_modal_forms.mixins import PopRequestMixin, CreateUpdateAjaxMixin

class AccountForm(PopRequestMixin, CreateUpdateAjaxMixin, forms.ModelForm):
    class Meta:
        model = Account
        exclude = ['timestamp']

