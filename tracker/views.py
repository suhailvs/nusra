from pathlib import Path

from django.http import HttpResponse, JsonResponse
from django.urls import reverse
from django.shortcuts import render, redirect, get_object_or_404
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
    return render(request, "tracker/home.html", {
        "medicines": medicines,
        "customer_form": CustomerForm(),
        "medicine_form": MedicineForm(),
    })


def add_customer(request):
    if request.method != "POST":
        return redirect("home")
    form = CustomerForm(request.POST)
    if form.is_valid():
        customer = form.save()
        return JsonResponse({"id": customer.pk, "name": customer.name, "phone": customer.phone})
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


def add_medicine(request):
    if request.method != "POST":
        return redirect("home")
    form = MedicineForm(request.POST)
    if form.is_valid():
        medicine = form.save()
        return JsonResponse({
            "id": medicine.pk,
            "name": medicine.name,
            "customer": medicine.customer.name,
            "phone": medicine.customer.phone,
            "delete_url": reverse("delete_medicine", args=[medicine.pk]),
        })
    return JsonResponse({"errors": form.errors.get_json_data()}, status=400)


def delete_medicine(request, pk):
    if request.method != "POST":
        return JsonResponse({"error": "POST required"}, status=405)
    medicine = get_object_or_404(Medicine, pk=pk)
    medicine.delete()
    return JsonResponse({"deleted": True})
