from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from core.apps.museum import models


class SymbolAdminForm(forms.ModelForm):
    class Meta:
        model = models.Symbol
        widgets = {
            "description": CKEditor5Widget(),
        }
        fields = "__all__"
