from django.shortcuts import render
from .forms import ImportForm
from transaction.models import ImportedStocks, Item, Transaction

def warehouse(request):
    
    if request.method == 'POST':
        form = ImportForm(request.POST)

        if(form.is_valid):
            print("VALIDATED")

            importform = form.cleaned_data
            date = importform.get("date")
            documentNumber = importform.get("documentNumber")
            name = importform.get("name")
            brand = importform.get("brand")
            price = importform.get("price")
            retailPrice = importform.get("retailPrice")
            quantity = importform.get("quantity")
            unit = importform.get("unit")


    context={
        'ImportForm':ImportForm(auto_id=False),
    }
    return render(request, "warehouse.html", context)