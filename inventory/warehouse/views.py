from django.shortcuts import render
from .forms import ImportForm
from transaction.models import ImportedStocks, Item, Transaction
from django.utils import timezone 
from django.contrib import messages


def warehouse(request):
    
    if request.method == 'POST':
        form = ImportForm(request.POST)

        if form.is_valid():
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

            try:
                item = Item.objects.get(name=name)
                item.quantityLeft+=quantity
                item.save()
            except(Item.DoesNotExist):
                messages.warning(request, "ITEM "+name+" DOES NOT EXIST")
                return redirect('/warehouse/')

            stock = ImportedStocks(
                date=date,
                documentNumber=documentNumber,
                quantity=quantity,
                transaction=transaction,
                item=item
            )

            stock.save()

            messages.success(request, "STOCKS ADDED")
        else:
            messages.warning(request, "INVALID INPUT")

        return redirect("/warehouse/")

    items = Item.objects.all()
    transactions = ImportedStocks.objects.all()

    context={
        'ImportForm':ImportForm(auto_id=False),
        'Items':items,
        'Transactions':transactions,
    }
    
    return render(request, "warehouse.html", context)