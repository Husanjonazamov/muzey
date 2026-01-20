from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from core.apps.museum import models


class ExhibitAdminForm(forms.ModelForm):
    class Meta:
        model = models.About
        widgets = {
            "text": CKEditor5Widget(),
        }
        fields = "__all__"

