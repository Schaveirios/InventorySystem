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

    
class SearchPurchaseForm(forms.Form):
    documentNumber = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'class':'form-control'}))


class ReturnForm(forms.Form):
    condition = forms.ChoiceField(choices=[
            ['Defective','defective'],
            ['Good Condition','good condition'],
        ], widget=forms.Select(attrs={"class":"form-control"}))
    dateReturned = forms.DateField(widget=forms.DateInput(attrs={'class':'form-control', 'type':'date'}))
    remark = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    quantity = forms.DecimalField(max_digits=10, decimal_places=2, widget=forms.NumberInput(attrs={"class":"form-control"}))
    purchaseId = forms.IntegerField(min_value=1, widget=forms.NumberInput(attrs={'style':'visibility:hidden;position:absolute;','id':'purchaseId'}))
    
    def __str__(self):
        return "Return Item"