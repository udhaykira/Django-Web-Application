from django import forms 
from .models import Item

class ItemForm(forms.ModelForm):
      class Meta:#tells us what feilds must be present in form
            model= Item #model for Item
            fields = ['item_name','item_desc','item_price','item_image']