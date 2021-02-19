from django import forms

from .models import Introduction

class introductionEdit(forms.ModelForm):
    class Meta:
        model = Introduction
        fields = ('text', 'image', 'location')
