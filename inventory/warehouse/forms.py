from django import forms


class ImportForm(forms.Form):
    date = forms.DateField(widget=forms.DateInput(attrs={
        'class':'form-control',
        'type':'date',
    }))
    documentNumber = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Doc. #',
    }))
    name = forms.CharField(max_length=200, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Item Name',
        'id':'item_name',
        'style':'visibility:hidden;position:fixed;',
    }))
    brand = forms.CharField(max_length=100, widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Brand',
        'id':'item_brand',
    }))
    price = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'wholesale price',
        'id':'item_wsp',
    }))
    retailPrice = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'retail price',
        'id':'item_srp',
    }))
    quantity = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={
        'class':'form-control',
        'placeholder':'Quantity',
        'id':'item_qty',
    }))
    unit = forms.ChoiceField(
        choices=[
            ['pcs','pcs'],
            ['pack','pack'],
        ], widget=forms.Select(attrs={
        'class':'form-control',
        'id':'item_unit'
    }))

    def __str__(self):
        return 'Import Item'