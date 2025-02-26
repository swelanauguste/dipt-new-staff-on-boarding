from django.db import models
from django.shortcuts import reverse


class Department(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, blank=True, null=True)

    def __str__(self):
        return self.name


class Status(models.Model):
    name = models.CharField(max_length=100)
    
    class Meta:
        verbose_name_plural = "Statuses"

    def __str__(self):
        return self.name


class Staff(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    middle_initial = models.CharField(max_length=1, blank=True, null=True)
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="departments"
    )
    key_access_pass = models.BooleanField(default=False)
    status = models.ForeignKey(
        Status,
        on_delete=models.CASCADE,
        related_name="statuses",
        null=True,
        blank=True,
    )
    role = models.CharField(max_length=100, blank=True, null=True)
    email = models.EmailField(unique=True, blank=True, null=True)
    same_role_as = models.CharField(max_length=100, blank=True, null=True)
    other = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        ordering = ["created_at"]

    def get_absolute_url(self):
        return reverse("staff-detail", kwargs={"pk": self.pk})

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
