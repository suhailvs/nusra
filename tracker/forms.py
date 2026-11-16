from django import forms
from .models import Customer, Medicine


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["name", "phone"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Customer name", "autofocus": True}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone (optional)", "inputmode": "tel"}),
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["customer", "name"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Medicine name"}),
        }
