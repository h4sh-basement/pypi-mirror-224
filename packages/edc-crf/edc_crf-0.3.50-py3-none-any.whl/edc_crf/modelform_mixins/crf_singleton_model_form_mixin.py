from __future__ import annotations

from typing import TYPE_CHECKING

from django import forms
from django.core.exceptions import ObjectDoesNotExist

if TYPE_CHECKING:
    from .crf_model_form_mixin import CrfModelFormMixin

    class MyForm(CrfModelFormMixin, forms.ModelForm):
        pass


class CrfSingletonModelFormMixin:
    def clean(self) -> dict:
        cleaned_data = super().clean()
        self.raise_if_singleton_exists()
        return cleaned_data

    def raise_if_singleton_exists(self: MyForm) -> None:
        """Raise if singleton model instance exists at another
        timepoint.
        """
        if not self.instance.id:
            opts = {
                f"{self.related_visit_model_attr}__subject_identifier": self.subject_identifier
            }
            try:
                obj = self._meta.model.objects.get(**opts)
            except ObjectDoesNotExist:
                pass
            else:
                raise forms.ValidationError(
                    f"Invalid.  This form has already been submittted. "
                    f"See '{obj.visit_code}.{obj.visit_code_sequence}'."
                )
