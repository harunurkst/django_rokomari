from django import forms
from .models import Category, Item

#
# class WriterForm(forms.ModelForm):
#     class Meta:
#         model = Writer
#         fields = '__all__'


class AddToCartForm(forms.ModelForm):
    qty = forms.IntegerField(initial=1)

    class Meta:
        model = Item
        fields = ('size', 'color', 'qty')

        widgets = {
            'size': forms.Select(attrs={'class': 'input-select'}),
            'color': forms.Select(attrs={'class': 'input-select'}),

        }