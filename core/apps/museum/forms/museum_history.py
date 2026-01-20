from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget
from core.apps.museum.models import MuseumHistory

class MuseumHistoryForm(forms.ModelForm):
    class Meta:
        model = MuseumHistory

        widgets = {
            "text": CKEditor5Widget(),
        }
        fields = "__all__"

