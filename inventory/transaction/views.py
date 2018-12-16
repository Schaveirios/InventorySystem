from django.shortcuts import render, redirect
from django.forms import formset_factory
from .forms import PurchaseForm, SearchPurchaseForm, ReturnForm
from django.utils import timezone
from .models import ImportedStocks, Item, Transaction, PurchasedItem, ReturnedItem
from django.contrib import messages
from django.contrib.auth.decorators import login_required

@login_required
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


@login_required
def return_item(request):
    context={
        'searchform':SearchPurchaseForm(),
        'return_form':ReturnForm(),
    }

    if(request.method=='POST'):
        form = ReturnForm(request.POST)
        if form.is_valid():
            returnitem = form.cleaned_data
            condition = returnitem.get("condition")
            dateReturned = returnitem.get("dateReturned")
            remark = returnitem.get("remark")
            quantity = returnitem.get("quantity")
            purchaseId = returnitem.get("purchaseId")

            try:
                purchased_item = PurchasedItem.objects.get(id=purchaseId)
            except(PurchasedItem.DoesNotExist):
                messages.warning(request, "Transaction Does Not Exist")
                return redirect('/transaction/return')            

            if(quantity>purchased_item.quantity):
                messages.warning(request, "Invalid quantity")
                return redirect('/transaction/return')

            transaction = Transaction(
                entryDate=dateReturned,
                nameOfTransaction=form.__str__()
            )
            transaction.save()

            if(condition=="good condition"):
                item = purchased_item.item
                item.quantityLeft+=quantity
                item.save()

            return_item = ReturnedItem(
                purchasedItem=purchased_item,
                dateReturned=dateReturned,
                condition=condition,
                remark=remark,
                quantity=quantity,
                transaction=transaction
            ) 
            
            return_item.save()

            transactions = PurchasedItem.objects.filter(transaction__id=purchased_item.transaction.id)
            total=0
            for purchase in transactions:
                total+=purchase.quantity*purchase.item.retailPrice

            context={
                'searchform':SearchPurchaseForm(),
                'transactions':transactions,
                'total':total,
                'return_form':ReturnForm(),
            }

            return render(request, 'return_item.html', context)

            messages.success(request, "Item returned")
            redirect("/transaction/return")
            
        else:
            messages.warning(request, "Invalid Input")
            return redirect("/transaction/return")

    return render(request, 'return_item.html', context)


@login_required
def search_purchase(request):
    if(request.method=='POST'):
        form = SearchPurchaseForm(request.POST)
        if form.is_valid():
            search = form.cleaned_data
            date = search.get("date")
            documentNumber = search.get("documentNumber")

            transactions = PurchasedItem.objects.filter(date=date, documentNumber=documentNumber)
            
            if(len(transactions)==0):
                messages.warning(request, "Transaction Does Not Exist")
                return redirect('/transaction/return')

            total=0
            for purchase in transactions:
                total+=purchase.quantity*purchase.item.retailPrice

            context={
                'searchform':SearchPurchaseForm(),
                'transactions':transactions,
                'total':total,
                'return_form':ReturnForm(),
            }
            return render(request, 'return_item.html', context)

        else:
            messages.warning(request, "Invalid Input")
            return redirect("/transaction/return")

    return redirect('/transaction/return')