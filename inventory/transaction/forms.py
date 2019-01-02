from django import forms


class PurchaseForm(forms.Form):
    date = forms.DateField()
    itemName = forms.CharField(max_length=100)
    brand = forms.CharField(max_length=100)
    documentNumber = forms.IntegerField(min_value=1)
    quantity = forms.DecimalField(max_digits=10, decimal_places=2)
    soldTo = forms.CharField(max_length=100)

    def __str__(self):
        return "Sold Item"
