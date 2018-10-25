from django.shortcuts import render
from .forms import ImportForm
from transaction.models import ImportedStocks, Item, Transaction
from django.utils import timezone 

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

            transaction = Transaction(
                entryDate=timezone.now(),
                nameOfTransaction=form.__str__()
            )

            transaction.save()

            item = Item.objects.get(name)
            item.quantity+=quantity
            item.save()

            stock = ImportedStocks(
                date=date,
                documentNumber=documentNumber,
                quantity=quantity,
                transaction=transaction,
                item=item
            )

    context={
        'ImportForm':ImportForm(auto_id=False),
    }
    
    return render(request, "warehouse.html", context)