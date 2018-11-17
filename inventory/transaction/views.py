from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import PurchaseForm
from django.utils import timezone
from .models import ImportedStocks, Item, Transaction, PurchasedItem
from django.contrib import messages


def sold_item(request):
    form = formset_factory(PurchaseForm, extra=20, max_num=20)
    purchases = PurchasedItem.objects.all()
    items = Item.objects.all()

    if(request.method == 'POST'):
        formset = form(request.POST, prefix="purchase")
        print(formset.errors)
        if formset.is_valid():

            transaction = Transaction(
                entryDate=timezone.now(),
                nameOfTransaction='Sold Item'
            )

            transaction.save()

            for loop_index, entry in enumerate(formset):
                if(not entry.has_changed()):
                    print(loop_index, entry.has_changed())
                    continue
                purchase = entry.cleaned_data
                date = purchase.get("date")
                itemName = purchase.get("itemName")
                brand = purchase.get("brand")
                documentNumber = purchase.get("documentNumber")
                quantity = purchase.get("quantity")
                soldTo = purchase.get("soldTo")

                try:
                    item = Item.objects.get(
                        name=itemName,
                        brand=brand
                    )
                    item.quantityLeft-=quantity
                    item.save()
                except(Item.DoesNotExist):
                    messages.warning(request, "ITEM "+itemName+" DOES NOT EXIST")
                    return redirect('/transaction/sold')

                sold = PurchasedItem(
                    date=date,
                    item=item,
                    documentNumber=documentNumber,
                    quantity=quantity,
                    soldTo=soldTo,
                    transaction=transaction
                )

                sold.save()

            messages.success(request, "Sold Item")
            return redirect("/transaction/sold")
        else:
            messages.warning(request, "Invalid Input: "+str(formset.errors))
            return redirect("/transaction/sold")
        
    else:
        formset = form(prefix="purchase")

    context = {
        'formset':formset,
        'purchases':purchases,
        'items':items,
    }

    return render(request, 'transaction/sold_item.html', context)


def return_item(request):
    return render(request, 'return_item.html')