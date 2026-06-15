from django import forms
from django_ckeditor_5.widgets import CKEditor5Widget

from core.apps.museum import models


class MothAdminForm(forms.ModelForm):
    class Meta:
        model = models.Moth
        widgets = {
            "text": CKEditor5Widget(),
        }
        fields = "__all__"
