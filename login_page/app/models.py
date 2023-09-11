import random
import string
from django.db import models
from django.contrib.auth.models import User

def generate_unique_referral_code():
    length = 6
    while True:
        code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))
        if not ReferralCode.objects.filter(code=code).exists():
            return code

class ReferralCode(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    code = models.CharField(max_length=10, unique=True, null=True, blank=True)
    referred_by = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, related_name='referrals')

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = generate_unique_referral_code()
        super().save(*args, **kwargs)
