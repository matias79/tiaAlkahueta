from django.forms import ModelForm
from .models import Menu

class MenuForm(ModelForm):
    class Meta:
        model = Menu
        field = '__all__'
        
    

