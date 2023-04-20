from django.db.models import fields
from django import forms
from .models import Votes

class Vote(forms.ModelForm):
    class Meta:
        model = Votes
        fields = "__all__"
