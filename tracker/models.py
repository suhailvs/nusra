from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=120)
    phone = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Medicine(models.Model):
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, related_name="medicines"
    )
    name = models.CharField(max_length=160)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return f"{self.name} ({self.customer})"
