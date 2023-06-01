from django.forms import ModelForm
from .models import Hit

class HitForm(ModelForm):
  class Meta:
    model = Hit
    fields = ['date', 'base']