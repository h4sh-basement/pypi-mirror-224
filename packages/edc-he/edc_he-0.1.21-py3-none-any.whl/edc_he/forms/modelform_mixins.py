from django import forms
from django.core.exceptions import ObjectDoesNotExist
from edc_constants.constants import YES

from ..utils import (
    get_assets_model_cls,
    get_household_head_model_cls,
    get_income_model_cls,
    get_patient_model_cls,
    get_property_model_cls,
)


class HealthEconomicsModelFormMixin:
    def clean(self):
        self.raise_if_he_household_head_required()
        self.raise_if_he_patient_required()
        self.raise_if_he_assets_required()
        self.raise_if_he_property_required()
        return super().clean()

    @property
    def household_head(self):
        return get_household_head_model_cls().objects.get(
            subject_visit__subject_identifier=self.subject_identifier
        )

    @property
    def is_hoh(self):
        return self.household_head.hoh == YES

    def raise_if_he_household_head_required(self):
        if self._meta.model != get_household_head_model_cls():
            try:
                self.household_head
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    f"Complete {get_household_head_model_cls()._meta.verbose_name} CRF first."
                )

    def raise_if_he_patient_required(self):
        if not self.is_hoh and self._meta.model in [
            get_assets_model_cls(),
            get_income_model_cls(),
            get_property_model_cls(),
        ]:
            try:
                get_patient_model_cls().objects.get(
                    subject_visit__subject_identifier=self.subject_identifier
                )
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    f"Complete {get_patient_model_cls()._meta.verbose_name} CRF first."
                )

    def raise_if_he_assets_required(self):
        if self._meta.model in [
            get_income_model_cls(),
            get_property_model_cls(),
        ]:
            try:
                get_assets_model_cls().objects.get(
                    subject_visit__subject_identifier=self.subject_identifier
                )
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    f"Complete {get_assets_model_cls()._meta.verbose_name} CRF first."
                )

    def raise_if_he_property_required(self):
        if self._meta.model in [
            get_income_model_cls(),
        ]:
            try:
                get_property_model_cls().objects.get(
                    subject_visit__subject_identifier=self.subject_identifier
                )
            except ObjectDoesNotExist:
                raise forms.ValidationError(
                    f"Complete {get_property_model_cls()._meta.verbose_name} CRF first."
                )
