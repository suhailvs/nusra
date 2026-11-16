from pathlib import Path

from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import CustomerForm, MedicineForm
from .models import Medicine


def service_worker(request):
    worker_path = Path(__file__).parent / "static" / "pwa" / "sw.js"
    response = HttpResponse(worker_path.read_text(), content_type="application/javascript")
    response["Service-Worker-Allowed"] = "/"
    response["Cache-Control"] = "no-cache"
    return response


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
