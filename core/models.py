from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    balance = models.DecimalField(max_digits=10, decimal_places=2, default=1000.00)  # Starting balance

    def __str__(self):
        return self.user.username

class Transfer(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name='sent_transfers')
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name='received_transfers')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} → {self.receiver} (${self.amount})"
