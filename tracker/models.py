from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=120, unique=True)
    phone = models.CharField(max_length=20, blank=True)

    class Meta:
        ordering = ["name"]

    def save(self, *args, **kwargs):
        normalized_name = self.name.lower()
        if normalized_name != self.name and kwargs.get("update_fields") is not None:
            kwargs["update_fields"] = set(kwargs["update_fields"]) | {"name"}
        self.name = normalized_name
        super().save(*args, **kwargs)

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
