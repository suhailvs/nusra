from django import forms
from .models import Customer, Medicine


class CustomerForm(forms.ModelForm):
    def clean_name(self):
        return self.cleaned_data["name"].lower()

    class Meta:
        model = Customer
        fields = ["name", "phone"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Customer name", "class": "form-control", "id": "customer_name"}),
            "phone": forms.TextInput(attrs={"placeholder": "Phone (optional)", "inputmode": "tel", "class": "form-control"}),
        }


class MedicineForm(forms.ModelForm):
    class Meta:
        model = Medicine
        fields = ["customer", "name"]
        widgets = {
            "name": forms.TextInput(attrs={"placeholder": "Medicine name", "class": "form-control", "id": "medicine_name"}),
            "customer": forms.Select(attrs={"class": "form-select"}),
        }
