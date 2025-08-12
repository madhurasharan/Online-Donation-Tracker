from django.db import models
from users.models import User

class Campaign(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    description = models.TextField()
    target_amount = models.DecimalField(max_digits=12, decimal_places=2)
    deadline = models.DateTimeField()
    media = models.ImageField(upload_to='campaign_media/', null=True, blank=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self): return self.title