from django.shortcuts import render, redirect
from .forms import CustomerForm, MedicineForm
from .models import Medicine


def home(request):
    medicines = Medicine.objects.select_related("customer")
    return render(request, "tracker/home.html", {"medicines": medicines})


def add_customer(request):
    form = CustomerForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "tracker/form.html", {"form": form, "title": "Add customer"})


def add_medicine(request):
    form = MedicineForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("home")
    return render(request, "tracker/form.html", {
        "form": form, "title": "Add medicine", "extra_link": True,
    })
