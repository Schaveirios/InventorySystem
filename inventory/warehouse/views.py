from django.shortcuts import render, redirect
from .forms import ImportForm, NewItemForm
from transaction.models import ImportedStocks, Item, Transaction
from django.utils import timezone 
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from user.views import log_activity 


@login_required
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
            
            log_activity(request,"Added "+str(stock.quantity)+" "+item.name, transaction.entryDate)
            
            messages.success(request, "STOCKS ADDED")
        else:
            messages.warning(request, "INVALID INPUT")

        return redirect("/warehouse/")

    items = Item.objects.all()
    transactions = ImportedStocks.objects.all()

    context={
        'ImportForm':ImportForm(auto_id=False),
        'NewItemForm':NewItemForm(auto_id=False),
        'Items':items,
        'Transactions':transactions,
    }
    
    return render(request, "warehouse.html", context)

@login_required
def add_item(request):

    if request.method == 'POST':
        form = NewItemForm(request.POST)
        if form.is_valid():
            
            itemform = form.cleaned_data
            name = itemform.get("name")
            distributor = itemform.get("distributor")
            brand = itemform.get("brand")
            price = itemform.get("price")
            retailPrice = itemform.get("retailPrice")
            unit = itemform.get("unit")

            item = Item(
                name=name,
                distributor=distributor,
                brand=brand,
                price=price,
                retailPrice=retailPrice,
                unit=unit,
                quantityLeft=0
            )

            item.save()
            log_activity(request,"Added new item, "+item.name, timezone.now())

            messages.success(request, "NEW ITEM ADDED")
        else:
            messages.warning(request, "INVALID FORM")
        
        return redirect('/warehouse/')
    return redirect('/warehouse/')
